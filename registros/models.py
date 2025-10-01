from django.db import models

class Registro(models.Model):
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    categoria = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.categoria} - {self.monto}"
