from django.contrib import admin
from .models import Education

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'status', 'start_year', 'end_year', 'order')
    list_editable = ('order',)
    list_filter = ('status', 'institution')
    search_fields = ('degree', 'institution')
