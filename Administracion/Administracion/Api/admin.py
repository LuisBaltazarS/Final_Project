from django.contrib import admin

from .models import Usuario, Tipo_user, Institucion, Director, Tutor, Tipo_user

class Lista_users(admin.ModelAdmin):

    list_display = ("id", "nombres", "apellidos", "tipo", "dni", "correo", "telefono", "fecha_nac")
    search_fields = ("nombres", "apellidos", "tipo__tipo", "dni")

class Lista_tutor(admin.ModelAdmin):

    list_display = ("nombres", "apellidos", "dni", "email", "institucion", "telefono", "fecha_nac")
    search_fields = ("nombres", "apellidos", "dni", "institucion__nombre")

class Lista_director(admin.ModelAdmin):

    list_display = ("nombres", "apellidos", "dni", "email", "telefono")
    search_fields = ("nombres", "apellidos", "dni")

class Lista_institucion(admin.ModelAdmin):

    list_display = ("nombre", "director", "cod_modular", "cod_local")
    search_fields = ("nombre", "director__nombre", "director__apellido", "cod_modular")

# Register your models here.

admin.site.register(Usuario, Lista_users)
admin.site.register(Tipo_user) 
admin.site.register(Institucion, Lista_institucion)
admin.site.register(Director, Lista_director)
admin.site.register(Tutor, Lista_tutor)