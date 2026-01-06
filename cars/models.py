from django.db import models

class Car(models.Model):
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('alugado', 'Alugado'),
        ('manutencao', 'Em Manutenção'),
    ]

    model = models.CharField('Modelo', max_length=100)
    plate = models.CharField('Placa', max_length=10, unique=True)
    year = models.IntegerField('Ano')
    km = models.IntegerField('Quilometragem', default=0)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='disponivel')

    purchase_price = models.DecimalField('Valor da compra', max_digits=10, decimal_places=2, null=True, blank=True)
    financed = models.BooleanField('Financiado', default=False)

    def __str__(self):
        return f"{self.model} - {self.plate}"
