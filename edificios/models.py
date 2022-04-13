from pyexpat import model
from django.db import models

class Switche(models.Model):
    name_switch=models.CharField(max_length=10)
    image_sw=models.ImageField()
    modelo=models.CharField(max_length=20)
    num_bocas=models.IntegerField()
    ip_gestion=models.CharField(max_length=20)
    comentario=models.CharField(max_length=40)

    def __str__(self):
        return self.name_switch

class Patchera(models.Model):
    montante=models.CharField(max_length=5)
    patchera=models.CharField(max_length=5)
    num_bocas=models.IntegerField()

    def __str__(self):
        return self.montante 

class Apartamento(models.Model):
    apartamento=models.CharField(max_length=10)
    nombreAP=models.CharField(max_length=20)
    dir_ip=models.CharField(max_length=20)
    mac_address=models.CharField(max_length=20)
    status=models.BooleanField()
    switch = models.ForeignKey(Switche, on_delete = models.CASCADE)
    boca_switch=models.IntegerField()
    patchera = models.ForeignKey(Patchera, on_delete = models.CASCADE)
    boca_patchera=models.IntegerField()

    def __str__(self):
        return self.apartamento



