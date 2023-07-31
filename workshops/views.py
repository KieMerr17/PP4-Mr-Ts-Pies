from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Workshop
from .forms import BookingForm

def book_workshop(request, workshop_id):
    workshop = Workshop.objects.get(pk=workshop_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.workshop = workshop
            booking.save()
            return redirect('workshop_detail', slug=workshop.slug)
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})


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
        