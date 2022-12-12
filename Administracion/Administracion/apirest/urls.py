from django.urls import path, re_path
from . import views

urlpatterns = [

    re_path(f'^usuarios/$', views.users_list),
    re_path(f'^administradores/$', views.admin_list),
    re_path(f'^reportes/$', views.reporte_list)
    
]