from . import views
from django.urls import path


urlpatterns = [
    path('', views.PieList.as_view(), name='pies'),
]