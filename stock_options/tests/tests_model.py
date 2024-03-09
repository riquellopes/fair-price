import pytest
from .factories import StockFactory, StockItemFactory
from stock_options.models import StockItem, Stock

@pytest.mark.django_db
def test_get_petra():
    petra = StockFactory()
    assert petra.ticket == "PETR4"

@pytest.mark.django_db
def test_create_an_item_and_get_average_price():
    item = StockItem(
        stock = StockFactory(),
        price = 2,
        quantity = 500,
        kind = "put"
    )
    item.save()

    petr = Stock.objects.get(pk=item.stock.id)
    # put_petra = StockItemFactory()
    # assert put_petra.ticket == "PETRP361"
    assert petr.average_price == 1000