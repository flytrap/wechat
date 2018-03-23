from django.contrib import admin
from .models import Notification


# Register your models here.

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_id', 'type', 'action', 'is_read')
    list_filter = ('project_id', 'type', 'action', 'is_read')
