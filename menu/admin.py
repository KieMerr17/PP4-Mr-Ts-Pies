from django.contrib import admin
from .models import Pie, Allergy
from django_summernote.admin import SummernoteModelAdmin


# register the Pie model to the admin panel
@admin.register(Pie)
class PiesAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('allergies', 'diet')
    list_display = ('title', 'diet')
    search_fields = ('title', 'allergies', 'diet')
    summernote_fields = ('description',)
