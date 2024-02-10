from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

KINDS = (
    ("stock", "Stock"),
    ("put", "Put"),
    ("call", "Call")
)

class Stock(models.Model):
    ticket = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    average_price = models.DecimalField(max_digits=5, decimal_places=2, default=0, editable=False)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.ticket

class StockItem(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    ticket = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    kind = models.CharField(max_length=200, choices=KINDS, default="stock")
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.ticket
    
@receiver(post_save, sender=StockItem)
def calc_average_price(sender, instance, *args, **kwargs):
    pass
