from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Pie


# Connect the Pie model to pies.html
class PieList(generic.ListView):
    model = Pie
    template_name = 'pies.html'


# Pie user like function
class PieLike(View):
    def post(self, request, slug):
        pie = get_object_or_404(Pie, slug=slug)
        if pie.likes.filter(id=request.user.id).exists():
            pie.likes.remove(request.user)
        else:
            pie.likes.add(request.user)

        return redirect('pies')
