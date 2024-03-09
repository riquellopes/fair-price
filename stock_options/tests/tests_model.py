import pytest
from .factories import StockFactory

@pytest.mark.django_db
def test_get_petra():
    petra = StockFactory()
    assert petra.ticket == "PETR4"