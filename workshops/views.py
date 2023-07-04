from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Workshop


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