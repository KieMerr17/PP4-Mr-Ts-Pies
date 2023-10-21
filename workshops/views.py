from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib import messages
from django.utils import timezone
from datetime import date
from .models import Workshop, Booking
from .forms import BookingForm
from django.db.models import F


def book_workshop(request, workshop_id):
    workshop = Workshop.objects.get(pk=workshop_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            # Associate the booking with the logged-in user
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking awaiting approval!')
            return redirect('profile')
    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {
        'form': form,
        'clicked_workshop': workshop.id,
    })


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    current_workshop = booking.workshop
    current_spaces = booking.spaces

    if request.method == 'POST':
        # get new input data from the form
        new_spaces = int(request.POST.get('spaces', 0))
        new_name = request.POST.get('name')
        new_email = request.POST.get('email')
        new_phone_number = request.POST.get('phone_number')
        new_diet = request.POST.get('dietary_requirements')

        space_diff = new_spaces - current_spaces
        available_spaces = current_workshop.spaces

        if booking.approved:
            if space_diff <= available_spaces:
                current_workshop.spaces -= space_diff
                # update each booking field individually
                booking.name = new_name
                booking.email = new_email
                booking.phone_number = new_phone_number
                booking.dietary_requirements = new_diet
                booking.spaces = new_spaces
                # save fields
                booking.save()
                current_workshop.save()
                messages.success(request, 'Booking updated successfully.')
                # redirect back to profile page
                return redirect('profile')
            else:
                messages.error(request, 'Too many spaces requested.')
        else:
            # revert to original booking details if fail POST
            booking.name = new_name
            booking.email = new_email
            booking.phone_number = new_phone_number
            booking.dietary_requirements = new_diet
            booking.spaces = new_spaces

            if booking.spaces > available_spaces:
                messages.error(request, 'Too many spaces requested.')
            else:
                booking.save()
                messages.success(request, 'Booking updated successfully.')
                # redirect back to profile page
                return redirect('profile')

    form = BookingForm(instance=booking, initial={'spaces': current_spaces})
    return render(request, 'edit_booking.html', {
        'form': form,
        'current_workshop': booking.workshop,
        'current_name': booking.name,
        'current_email': booking.email,
        'current_phone_number': booking.phone_number,
        'current_diet': booking.dietary_requirements,
        'current_spaces': booking.spaces,
    })


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking deleted successfully.')
        # Redirect to the user's profile page
        return redirect('profile')

    return render(request, 'delete_booking.html', {'booking': booking})


# register the Workshop model on workshops.html
class WorkshopList(generic.ListView):
    model = Workshop
    template_name = 'workshops.html'
    paginate_by = 4

    def get_queryset(self):
        # Only show future events
        queryset = Workshop.objects.filter(
            event_date__gt=date.today()).order_by('event_date')

        # Update the status of past workshops to 0
        past_workshops = Workshop.objects.filter(event_date__lt=timezone.now())
        past_workshops.update(status=0)

        return queryset


class WorkshopDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Workshop.objects.filter(status=1)
        workshop = get_object_or_404(queryset, slug=slug)
        liked = False

        if workshop.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "workshop_detail.html",
            {
                "workshop": workshop,
                "liked": liked
            }
        )
