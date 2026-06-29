from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'created_at')
    readonly_fields = ('full_name', 'email', 'subject', 'message', 'created_at')
    search_fields = ('full_name', 'email', 'subject')
    date_hierarchy = 'created_at'

    # Disable addition of contact messages from admin panel manually
    def has_add_permission(self, request):
        return False
        
    # Optional: Disable change/edit from admin panel, only allow deletion
    def has_change_permission(self, request, obj=None):
        return False
