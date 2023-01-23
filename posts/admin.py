from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_at']
    list_filter=['title','created_at']
    search_fields=['title']