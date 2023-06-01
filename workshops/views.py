from django.shortcuts import render
from django.views import generic
from .models import Workshop


class WorkshopList(generic.ListView):
    model = Workshop
    queryset = Workshop.objects.filter(status=1).order_by('-created_on')
    template_name = 'workshops.html'
    paginate_by = 4

