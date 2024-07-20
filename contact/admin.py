from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phone', 'message')
    search_fields = ('fullname', 'email')