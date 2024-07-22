from django.contrib import admin
from .models import MenuCategory, MenuItem
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(MenuItem)
class MenuItemAdmin(SummernoteModelAdmin):
    list_display = ('name', 'category', 'formatted_description', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    summernote_fields = ('description',)
    
    def formatted_description(self, obj):
        return format_html(obj.description)
    formatted_description.short_description = 'Description'
