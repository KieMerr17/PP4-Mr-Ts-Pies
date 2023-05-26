from django.contrib import admin
from .models import Workshop, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Workshop)
class WorkshopAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'event_date', 'created_on')
    list_display = ('title', 'slug', 'chef','event_date', 'spaces', 'created_on', )
    search_fields = ('title', 'content')
    summernote_fields = ('content')


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('name', 'phone_number', 'workshop', 'spaces', 'dietary_requirements', 'booked_on', 'approved')
    list_filter = ('booked_on', 'approved')
    search_fields = ('name', 'email')
    actions = ['approve_booking']

    def approve_booking(self, request, queryset):
        queryset.update(approved=True)
