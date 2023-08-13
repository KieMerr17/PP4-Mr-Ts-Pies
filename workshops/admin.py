from django.contrib import admin, messages
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
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'phone_number', 'workshop', 'spaces', 'dietary_requirements', 'booked_on', 'approved')
    list_filter = ('booked_on', 'approved')
    search_fields = ('name', 'email')
    actions = ['Approve_selected', 'Delete_selected']

    def get_actions(self, request):
        actions = super().get_actions(request)
        del actions['delete_selected']
        return actions

    def Approve_selected(self, request, queryset):
        for booking in queryset:
            if not booking.approved:
                booking.approved = True
                new_spaces = booking.workshop.spaces - booking.spaces
                if new_spaces < 0:
                    messages.error(request, f"Spaces for this booking exceed the spaces available.")
                else:
                    booking.workshop.spaces = new_spaces
                    booking.workshop.save()
                    booking.save()
