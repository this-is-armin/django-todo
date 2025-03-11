from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ['id', 'finished', 'created', 'updated']
	list_filter = ['id', 'created', 'finished', 'updated']
	