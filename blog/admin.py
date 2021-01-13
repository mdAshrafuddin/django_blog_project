from django.contrib import admin
from .models import Post

# Register your models here.

def make_published(modeladmin, request, queryset):
    queryset.update(status=0)
make_published.short_description = "Mark selected stories as published"

class AdminPost(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'status')
    search_fields = ('title','content')
    list_filter = ('status',)
    prepopulated_fields = {"slug": ("title",)}
    actions = [make_published]
    change_form_template = 'admin/preview_template.html'
    

admin.site.register(Post, AdminPost)
