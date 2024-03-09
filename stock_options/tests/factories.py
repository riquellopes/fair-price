import factory

from stock_options.models import Stock


class StockFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = Stock
        django_get_or_create = ('ticket', )
    ticket = "PETR4"
    price = 1.0