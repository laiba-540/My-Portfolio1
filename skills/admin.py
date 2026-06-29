from django.contrib import admin
from .models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'category', 'order')
    list_editable = ('proficiency', 'category', 'order')
    list_filter = ('category',)
    search_fields = ('name', 'category')
