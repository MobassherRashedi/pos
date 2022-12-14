from django.db import models
from datetime import datetime

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
