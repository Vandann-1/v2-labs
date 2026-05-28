from django.contrib import admin

from .models import ProjectLead


@admin.register(ProjectLead)
class ProjectLeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "service", "budget", "ip_address", "created_at")
    search_fields = ("name", "email", "phone", "service", "message")
    list_filter = ("service", "created_at")
    readonly_fields = ("created_at", "ip_address", "user_agent", "source_page")
