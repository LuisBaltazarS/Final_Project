from django.contrib import admin

from .models import Usuario, Admin, Reporte

class Lista_admin(admin.ModelAdmin):

    list_display = ("id", "nombres", "apellidos", "dni", "correo", "password")
    search_fields = ("nombres", "apellidos", "dni")

class Lista_users(admin.ModelAdmin):

    list_display = ("id", "nombres", "apellidos", "dni", "correo", "password", "user_role")
    search_fields = ("nombres", "apellidos", "dni")

class Lista_reporte(admin.ModelAdmin):

    list_display = ("id", "filename", "id_usuario", "fecha_emitido", "estado")
    search_fields = ("filename", "id_usuario", "fecha_emitido", "estado")

# Register your models here.

admin.site.register(Usuario, Lista_users)
admin.site.register(Admin, Lista_admin)
admin.site.register(Reporte)