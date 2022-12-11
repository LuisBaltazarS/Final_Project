from django.contrib import admin

from .models import Usuario, Admin

class Lista_admin(admin.ModelAdmin):

    list_display = ("id", "nombres", "apellidos", "tipo", "dni", "correo", "telefono")
    search_fields = ("nombres", "apellidos", "tipo__tipo", "dni")

class Lista_users(admin.ModelAdmin):

    list_display = ("id", "nombres", "apellidos", "tipo", "dni", "correo", "telefono", "fecha_nac")
    search_fields = ("nombres", "apellidos", "tipo__tipo", "dni")

# Register your models here.

admin.site.register(Usuario, Lista_users)
admin.site.register(Admin)