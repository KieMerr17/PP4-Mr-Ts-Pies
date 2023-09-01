from django.shortcuts import render
from django.views import generic
from .models import Pie


class PieList(generic.ListView):
    model = Pie
    template_name = 'pies.html'