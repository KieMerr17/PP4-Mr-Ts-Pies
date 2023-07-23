from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic import ListView, DetailView, CreateView
from .models import Workshop, Booking

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

class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-booked_on')


# View to create a new booking for the logged-in user
class BookingCreateView(CreateView):
    model = Booking
    template_name = 'booking_form.html'
    fields = ['workshop', 'name', 'email', 'phone_number', 'spaces', 'dietary_requirements']
    success_url = '/bookings/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workshop_list'] = Workshop.objects.all()  # Fetch all workshops and add them to the context
        context['dietary_requirements'] = Booking.objects.values_list('dietary_requirements', flat=True).distinct()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# View to display details of a specific booking for the logged-in user
class BookingDetailView(DetailView):
    model = Booking
    template_name = 'booking_detail.html'
    context_object_name = 'booking'