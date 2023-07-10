from django.contrib import admin
from .models import Article
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Article)
class NewsAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'author')
    list_display = ('title', 'slug', 'author', 'created_on')
    search_fields = ('title', 'content')
    summernote_fields = ('content')

