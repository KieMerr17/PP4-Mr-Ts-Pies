from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.WorkshopList.as_view(), name='workshops'),
    path('<slug:slug>/', views.WorkshopDetail.as_view(), name='workshop_detail'),
    path('bookings/', login_required(views.BookingListView.as_view()), name='booking_list'),
    path('bookings/create/', login_required(views.BookingCreateView.as_view()), name='booking_create'),
    path('bookings/<int:pk>/', login_required(views.BookingDetailView.as_view()), name='booking_detail'),
]