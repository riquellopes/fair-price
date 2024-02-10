from typing import Any
from django.core.management.base import BaseCommand
from stock_options.models import Stock, process_the_average_price

class Command(BaseCommand):
    help = "Calculator average price for all stocks"

    def handle(self, *args: Any, **options: Any):
        for stock in Stock.objects.all():
            average_price = process_the_average_price(stock.id)
            stock.average_price = average_price
            stock.save()
            self.stdout.write(f"The stock {stock.ticket} was updated.")