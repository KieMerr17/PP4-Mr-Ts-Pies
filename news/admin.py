from django.contrib import admin
from .models import Article, Comment
from django_summernote.admin import SummernoteModelAdmin


# register the Article model to the admin panel
@admin.register(Article)
class NewsAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'author')
    list_display = ('title', 'slug', 'author', 'created_on')
    search_fields = ('title', 'content')
    summernote_fields = ('content')


# register the Comment model to the admin panel for news app
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'body', 'created_on')
    list_filter = ('post', 'created_on')
    search_fields = ('name', 'email', 'body')
