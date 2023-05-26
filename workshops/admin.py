from django.contrib import admin
from .models import Workshop, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Workshop)
class WorkshopAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'event_date', 'created_on')
    list_display = ('title', 'slug', 'chef', 'event_date', 'created_on')
    search_fields = ('title', 'content')
    summernote_fields = ('content')


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'booked_on', 'approved')
    list_filter = ('booked_on', 'approved')
    search_fields = ('name', 'email')

    
