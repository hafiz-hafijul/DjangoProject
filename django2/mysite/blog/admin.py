from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'create', 'updated']
    search_fields = ['title', 'body']
    list_filter = ['author', 'publish', 'create']
    prepopulated_fields = {'slug':['title']}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']