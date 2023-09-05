from django.contrib import admin
from .models import Task


@admin.register(Task)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id"
    )
