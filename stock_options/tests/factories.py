import factory

from stock_options.models import Stock, StockItem


class StockFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = Stock
        django_get_or_create = ('ticket', )
    ticket = "PETR4"
    price = 4.0
    quantity = 100


class StockItemFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = StockItem
        django_get_or_create = ('ticket', )
    stock = factory.SubFactory(StockFactory)
    ticket = "PETRP361"
    kind = "put"
    price = 1.0
    quantity = 100