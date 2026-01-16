from django.db import models

class Client(models.Model):
    name = models.CharField('Nome', max_length=100)
    phone = models.CharField('Telefone', max_length=20)
    cnh = models.CharField('Cnh', max_length=20, unique=True)

    def __str__(self):
        return f"{self.name}"