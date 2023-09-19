from . import views
from django.urls import path


urlpatterns = [
    path('', views.PieList.as_view(), name='pies'),
    path('like/<slug:slug>', views.PieLike.as_view(), name='pie_like'),
]