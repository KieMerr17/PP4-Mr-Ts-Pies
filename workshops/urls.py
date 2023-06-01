from . import views
from django.urls import path


urlpatterns = [
    path('', views.WorkshopList.as_view(), name='workshops')
]