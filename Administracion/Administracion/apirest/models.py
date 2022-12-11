from django.db import models

# Create your models here.

class Admin(models.Model): 

    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres', max_length=200, blank=False, null=False)
    apellidos = models.CharField('Apellidos', max_length=200, blank=False, null=False)
    dni = models.CharField('DNI', max_length=8, unique=True, blank=False, null=False)
    correo = models.EmailField('Correo electronico', max_length=200, unique=True ,blank=False, null=False)
    password = models.CharField('Contraseña', max_length=200, blank=False, null=False)

    class Meta:

        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"

    def __str__(self):
        return self.apellidos + ", " + self.nombres

class Usuario(models.Model):

    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres', max_length=200, blank=False, null=False)
    apellidos = models.CharField('Apellidos', max_length=200, blank=False, null=False)
    dni = models.CharField('DNI', max_length=8, unique=True, blank=False, null=False)
    correo = models.EmailField('Correo electronico', max_length=200, unique=True ,blank=False, null=False)
    password = models.CharField('Contraseña', max_length=200, blank=False, null=False)

    class Meta: 

        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"            

    def __str__(self):
        return self.apellidos + ", " + self.nombres

