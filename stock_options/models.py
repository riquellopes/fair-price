from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save

KINDS = (
    ("stock", "Stock"),
    ("put", "Put"),
    ("call", "Call")
)

STATUS = (
    ("done", "Done"),
    ("evaluate", "Evaluate"),
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
    status = models.CharField(max_length=200, choices=STATUS, default="evaluate")
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.ticket
    
    def is_an_option_evaluable(self) -> bool:
        return self.kind in ["call", "put"] and self.status == "evaluate"

    def is_a_stock_evaluable(self) -> bool:
        return self.kind == "stock" and self.status == "evaluate"
    
@receiver(pre_save, sender=StockItem)
def calc_average_price(sender, instance, *args, **kwargs):
    # total_price_item = instance.price * instance.quantity
    # total_price_stock = instance.stock.average_price * instance.stock.quantity
    # total_quantity = instance.quantity + instance.stock.quantity

    stock_average_price = instance.stock.average_price if instance.stock.average_price > 0 else instance.stock.price

    if instance.is_an_option_evaluable():
        instance.stock.average_price = stock_average_price - instance.price
        instance.stock.save()
    instance.status = "done"