from . import views
from django.urls import path


urlpatterns = [
    path('', views.WorkshopList.as_view(), name='workshops'),
    path('<slug:slug>/', views.WorkshopDetail.as_view(), name='workshop_detail'),
    path('workshop/<int:workshop_id>/book/', views.book_workshop, name='book_workshop'),
]
