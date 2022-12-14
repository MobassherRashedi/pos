from django.contrib import admin

# Register your models here.
from .models import SendEmail,SendSms

admin.site.register(SendSms)
admin.site.register(SendEmail)