from django.db import models
from django.conf import settings

# Create your models here.
class Masa(models.Model):
    MESE_CATEGORII = [
        ("M1", "Masa 1"),
        ("M2", "Masa 2"),
    ]

    masa = models.CharField(max_length=7, choices=MESE_CATEGORII)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"Masa {self.get_masa_display()} - Price: {self.price} RON"

class Rezervare(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    masa = models.ForeignKey(Masa, on_delete=models.CASCADE)
    check_in = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  


    def __str__(self):
        return f"{self.user} a rezervat {self.masa} in data de {self.check_in} pentru {self.price} RON"


