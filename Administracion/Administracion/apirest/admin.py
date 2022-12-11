from django.contrib import admin

from .models import Usuario, Admin

class Lista_admin(admin.ModelAdmin):

    list_display = ("id", "nombres", "apellidos", "dni", "correo", "password")
    search_fields = ("nombres", "apellidos", "dni")

class Lista_users(admin.ModelAdmin):

    list_display = ("id", "nombres", "apellidos", "dni", "correo", "password")
    search_fields = ("nombres", "apellidos", "dni")

# Register your models here.

admin.site.register(Usuario, Lista_users)
admin.site.register(Admin)