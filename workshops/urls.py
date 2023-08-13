from . import views
from django.urls import path


urlpatterns = [
    path('', views.WorkshopList.as_view(), name='workshops'),
    path('<slug:slug>/', views.WorkshopDetail.as_view(), name='workshop_detail'),
    path('workshop/<int:workshop_id>/book/', views.book_workshop, name='book_workshop'),
    path('booking/<int:booking_id>/edit/', views.edit_booking, name='edit_booking'),
    path('booking/<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),
]
