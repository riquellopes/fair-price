import datetime
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save

KINDS = (
    ("stock", "Stock"),
    ("put", "Put"),
    ("call", "Call"),
    ("div", "Dividends"),
)

STATUS = (
    ("done", "Done"),
    ("evaluate", "Evaluate"),
)

POCKETED = (
    ("y", "Yes"),
    ("n", "No"),
)

class Stock(models.Model):
    ticket = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    average_price = models.DecimalField(max_digits=5, decimal_places=2, default=0, editable=False)
    pocketed = models.CharField(max_length=200, choices=POCKETED, default="yes")
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.ticket

def process_the_average_price(stock_id: int):
    average_price = Stock.objects.raw(f"""
        SELECT sos.price - (sum(total)/sos.quantity) as average_price, sos.id  FROM (
            SELECT price*quantity as total, stock_id
            FROM stock_options_stockitem s WHERE s.stock_id = {stock_id}) as total_earnings JOIN 
        stock_options_stock sos ON total_earnings.stock_id = sos.id
    """)[0].average_price

    print("BBBB", average_price)
    
    return 0 if average_price is None else average_price


class StockItem(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    ticket = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    kind = models.CharField(max_length=200, choices=KINDS, default="stock")
    status = models.CharField(max_length=200, choices=STATUS, default="evaluate")
    quantity = models.IntegerField(default=0)
    payment_date = models.DateField(default=datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.ticket
    
    def is_an_option_evaluable(self) -> bool:
        return self.kind in ["call", "put", "div"] and self.status == "evaluate"

    def is_a_stock_evaluable(self) -> bool:
        return self.kind == "stock" and self.status == "evaluate"
    
@receiver(pre_save, sender=StockItem)
def calc_average_price(sender, instance, *args, **kwargs):
    if instance.is_an_option_evaluable():
        average_price = process_the_average_price(instance.stock.id)
        instance.stock.average_price = average_price if average_price > 0 else instance.stock.price

        instance.stock.save()
    instance.status = "done"