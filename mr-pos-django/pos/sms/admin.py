from django.contrib import admin

from .models import SendSms, SendEmail


@admin.register(SendSms)
class SendSmsAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'customer', 'message')
    list_filter = ('created_at', 'updated_at', 'customer')
    date_hierarchy = 'created_at'


@admin.register(SendEmail)
class SendEmailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'email',
        'subject',
        'message',
        'file',
    )
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'