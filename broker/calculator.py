from broker.models import Broker

class CalculatorParams:
    
    def __init__(self, strike_amount, reward, average_stock_price, quantity, operation_type) -> None:
        self.strike_amount = strike_amount
        self.reward = reward
        self.average_stock_price = average_stock_price
        self.quantity = quantity
        self.operation_type = operation_type

class Calculator:
    
    def __init__(self, broker: Broker, calc_params: CalculatorParams):
        self._broker = broker
        self._calc_params = calc_params
    
    def get_final_cost(self) -> float:
        return 0
    

class Option:

    def __init__(self, flat_tax, fromm, to, size):
        self._flat_tax = flat_tax
        self._from = fromm
        self._to = to
        self._size = size

    

def get_tax(broker: Broker, transaction_vol: float) -> Option:
    """
        Função deve apenas recuperar a taxa que precisa ser aplicada, não vai fazer nenhum cálculo.
    """
    for tax in broker.get_all_options():
        if tax.fromm == 0 and transaction_vol > tax.fromm:
            return Option(tax.flat_tax, tax.fromm, tax.to, tax.size)
        elif tax.fromm <= transaction_vol <= tax.to:
            return Option(tax.flat_tax, tax.fromm, tax.to, tax.size)
    return None