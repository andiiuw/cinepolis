from django.db import models

from django.contrib import admin

class Camion(models.Model):
    marca  =   models.CharField(max_length=200)
    modelo  =   models.CharField(max_length=200)
    matricula  =   models.CharField(max_length=50)
    tipo =   models.CharField(max_length=200)


    def __str__(self):
        return self.marca


class Piloto(models.Model):
    camion = models.ForeignKey('Camion', on_delete=models.CASCADE)
    nombre  =   models.CharField(max_length=200)
    direccion  =   models.CharField(max_length=200)
    telefono  =   models.CharField(max_length=50)
    salario  =   models.CharField(max_length=60)


    def __str__(self):
        return self.nombre

class Paquete(models.Model):
    piloto = models.ForeignKey('Piloto', on_delete=models.CASCADE)
    destinatario  =   models.CharField(max_length=200)
    direccion  =   models.CharField(max_length=200)
    descripcion  =   models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Ciudad(models.Model):
    nombre  =   models.CharField(max_length=200)
    paquete  = models.ManyToManyField(Paquete, through='Asignacion')

    def __str__(self):
        return self.nombre

class Asignacion(models.Model):
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    ciudad= models.ForeignKey(Ciudad, on_delete=models.CASCADE)



class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1


class CiudadAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)


# Create your models here.
