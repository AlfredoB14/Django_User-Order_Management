from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre=models.CharField(max_length=60)
    email=models.TextField()
    password=models.CharField(max_length=20)
    permission=models.TextChoices("Client", "Admin")

    def __str__(self):
        return self.name

class Lote():  #Lote
    #ID??
    cajas = models.IntegerChoices("5", "10", "15" "20", "25", "50")
    unidadesPorCaja = models.IntegerChoices("10", "15", "20")
    nombreUsuario = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.TextField(default="Confirmar")
    direccionEntrega = models.TextField()

    def __str__(self):
        return self.name
