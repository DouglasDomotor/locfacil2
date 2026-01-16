from django.db import models


class MaintenanceType(models.TextChoices):
    REVISAO = "REVISAO", "Revisão"
    OLEO = "OLEO", "Troca de óleo"
    FREIO = "FREIO", "Freios"
    CORREIA = "CORREIA", "Correia"
    SUSPENSAO = "SUSPENSAO", "Suspensão"
    OUTRO = "OUTRO", "Outro"
    PNEU = "PNEU", "Troca de pneus"




class Maintenance(models.Model):
    car = models.ForeignKey(
        "cars.Car",
        on_delete=models.PROTECT,
        related_name="maintenances"
    )

    type = models.CharField(
        max_length=20,
        choices=MaintenanceType.choices
    )

    km = models.PositiveIntegerField(
        help_text="Quilometragem do veículo no momento da manutenção"
    )

    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    date = models.DateField()

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]
        indexes = [
            models.Index(fields=["car", "date"]),
            models.Index(fields=["car", "km"]),
        ]

    def __str__(self):
        return f"{self.car} - {self.get_type_display()} ({self.km} km)"
