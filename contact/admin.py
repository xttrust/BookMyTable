from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('fullname', 'email', 'phone', 'message')
    
    # Fields to include in the search functionality in the admin interface
    search_fields = ('fullname', 'email')
