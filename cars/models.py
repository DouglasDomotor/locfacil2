from django.db import models

class Car(models.Model):
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('alugado', 'Alugado'),
        ('manutencao', 'Em Manutenção'),
    ]

    model = models.CharField(max_length=100)
    plate = models.CharField(max_length=10, unique=True)
    year = models.IntegerField()
    km = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')

    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    financed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.model} - {self.plate}"
