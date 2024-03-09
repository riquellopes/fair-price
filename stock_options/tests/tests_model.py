import pytest
from .factories import StockFactory, StockItemFactory
from stock_options.models import StockItem, Stock

@pytest.mark.django_db
def test_get_petra():
    petra = StockFactory()
    assert petra.ticket == "PETR4"

@pytest.mark.django_db
@pytest.mark.skip
def test_create_an_item_and_get_average_price():
    stock = StockFactory()
    item = StockItem(
        stock = stock,
        price = 0.5,
        quantity = 500,
        kind = "put"
    )
    item.save()
    # item.refresh_from_db()
    # stock.refresh_from_db()

    petr = Stock.objects.get(pk=item.stock.id)
    # put_petra = StockItemFactory()
    # assert put_petra.ticket == "PETRP361"
    assert petr.average_price == 1000