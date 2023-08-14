from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib import messages
from .models import Workshop, Booking
from .forms import BookingForm
from django.db.models import F


def book_workshop(request, workshop_id):
    workshop = Workshop.objects.get(pk=workshop_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Associate the booking with the logged-in user
            booking.save()
            messages.success(request, 'Booking awaiting approval!')
            return redirect('profile')
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    current_workshop = booking.workshop
    current_spaces = booking.spaces

    if request.method == 'POST':
        new_spaces = int(request.POST.get('spaces', 0))
        space_diff = new_spaces - current_spaces
        available_spaces = current_workshop.spaces


        if booking.approved:
            if space_diff <= available_spaces:
                current_workshop.spaces -= space_diff
                booking.spaces = new_spaces
                booking.save()
                current_workshop.save()
                messages.success(request, 'Booking updated successfully.')
                return redirect('profile')
            else:
                messages.error(request, 'Too many spaces requested.')
        else:
            booking.spaces = new_spaces
            if booking.spaces > available_spaces:
                messages.error(request, 'Too many spaces requested.')
            else:
                booking.save()
                messages.success(request, 'Booking updated successfully.')
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
        return redirect('profile')  # Redirect to the user's profile page
    return render(request, 'delete_booking.html', {'booking': booking})


class WorkshopList(generic.ListView):
    model = Workshop
    queryset = Workshop.objects.filter(status=1).order_by('event_date')
    template_name = 'workshops.html'
    paginate_by = 4


class WorkshopDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Workshop.objects.filter (status=1)
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
