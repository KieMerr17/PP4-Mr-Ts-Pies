from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib import messages
from .models import Workshop, Booking
from .forms import BookingForm


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
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = BookingForm(instance=booking)
    return render(request, 'edit_booking.html', {'form': form})


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
