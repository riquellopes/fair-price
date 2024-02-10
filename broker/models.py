from django.db import models


class Broker(models.Model):
    name = models.CharField(max_length=200)
    tax = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return self.name

    # def get_all_options(self) -> tuple[Options]:
    #     return None


class Options(models.Model):
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    flat_tax = models.DecimalField(max_digits=5, decimal_places=2)
    fromm = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="from")
    to = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.broker.name} R$ {self.flat_tax} fixo'