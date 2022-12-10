from django.db import models

# Create your models here.

class Admin(models.Model): 

    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres', max_length=200, blank=False, null=False)
    apellidos = models.CharField('Apellidos', max_length=200, blank=False, null=False)
    dni = models.CharField('DNI', max_length=8, unique=True, blank=False, null=False)
    correo = models.EmailField('Correo electronico', max_length=200, unique=True ,blank=False, null=False)
    password = models.CharField('Contraseña', max_length=200, blank=False, null=False)
    telefono = models.CharField('Telefono', max_length=9, unique=True, blank=False, null=False)

    class Meta:

        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"

    def __str__(self):
        return self.apellidos + ", " + self.nombres

class Tipo_user(models.Model):

    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=200)

    class Meta: 

        verbose_name = "Tipo de usuario"
        verbose_name_plural = "Tipos de usuarios"

    def __str__(self):
        return self.tipo

class Director(models.Model):

    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres', max_length=200, blank=False, null=False)
    apellidos = models.CharField('Apellidos', max_length=200, blank=False, null=False)
    dni = models.CharField('DNI', max_length=8, blank=False, null=False, unique=True)
    email = models.EmailField('Email', max_length=200, blank=False, null=False, unique=True)
    telefono = models.CharField('Telefono', max_length=9, blank=False, null=False, unique=True)

    class Meta: 

        verbose_name = "Director"
        verbose_name_plural = "Directores"

    def __str__(self):
        return self.apellidos + ", " + self.nombres

class Institucion(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del colegio', max_length=200, blank=False, null=False)
    director = models.OneToOneField(Director, on_delete=models.CASCADE)
    cod_modular = models.CharField('Código Modular', max_length=7, blank=False, null=False, unique=True)
    cod_local = models.CharField('Código Local', max_length=6, blank=False, null=False, unique=True)

    class Meta: 

        verbose_name = "Institucion"
        verbose_name_plural = "Instituciones"

    def __str__(self):
        return self.nombre

class Tutor(models.Model): 

    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres', max_length=200, blank=False, null=False)
    apellidos = models.CharField('Apellidos', max_length=200, blank=False, null=False)
    fecha_nac = models.DateField('Fecha de nacimiento')
    dni = models.CharField('DNI', max_length=8, unique=True, blank=False, null=False)
    email = models.CharField('Correo electronico', max_length=200, blank=False, null=False, unique=True)
    password = models.CharField('Contraseña', max_length=200, blank=False, null=False)
    telefono = models.CharField('Telefono', max_length=9, blank=False, null=False)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)

    class Meta: 

        verbose_name = "Tutor"
        verbose_name_plural = "Tutores"

    def __str__(self):

        return self.apellidos + ", " + self.nombres

class Usuario(models.Model):

    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres', max_length=200, blank=False, null=False)
    apellidos = models.CharField('Apellidos', max_length=200, blank=False, null=False)
    fecha_nac = models.DateField('Fecha de nacimiento', blank=False, null=False)
    dni = models.CharField('DNI', max_length=8, unique=True, blank=False, null=False)
    correo = models.EmailField('Correo electronico', max_length=200, unique=True ,blank=False, null=False)
    password = models.CharField('Contraseña', max_length=200, blank=False, null=False)
    telefono = models.CharField('Telefono', max_length=9, unique=True, blank=False, null=False)
    tipo = models.ForeignKey(Tipo_user, on_delete = models.CASCADE)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

    class Meta: 

        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"            

    def __str__(self):
        return self.apellidos + ", " + self.nombres

