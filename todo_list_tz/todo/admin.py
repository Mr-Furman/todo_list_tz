from django.contrib import admin
from .models import Task, Tag


@admin.register(Task)
class Task(admin.ModelAdmin):
    search_fields = ("contex",)


admin.site.register(Tag)
