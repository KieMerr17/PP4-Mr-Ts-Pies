from django.contrib import admin
from .models import Workshop, Comment, Make_Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Workshop)
class WorkshopAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
