from django.db import models
from pos.g_model import TimeStampMixin
from django.utils.translation import gettext as _



class Asset(TimeStampMixin):
    name = models.CharField(max_length=200,blank=False,null=False)
    amount = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False,default=0.00)
    note = models.CharField(max_length=250, blank=True,null=True)
    
    class Meta:
        verbose_name = _('Asset')
        verbose_name_plural = _('Asset')
        
    def __str__(self) -> str:
        return f"{self.id}"