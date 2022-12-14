from django.db import models
from pos.g_model import TimeStampMixin
from product.models import Product
from datetime import datetime
from django.utils.translation import gettext as _

class Damages(TimeStampMixin):
    date = models.DateTimeField(blank=False,null=True,default=datetime.now())
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    damage_qty = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    note = models.CharField(max_length=350, blank=True, null=True)
    # stock = models.CharField(max_length=350, blank=True, null=True) # this sould be come from product model.
    class Meta:
        verbose_name = _('Damage')
        verbose_name_plural = _('Damage')
        
    def __str__(self) -> str:
        return f"{self.id}"
    