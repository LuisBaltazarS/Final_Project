from django.urls import path, re_path
from .views import TipoUserView, DirectorView, InstitucionView, TutorView
from . import views

urlpatterns = [

    re_path(f'^usuarios/$', views.users_list),
    path('tipos/', TipoUserView.as_view(), name="userstype_list"),
    path('tipos/<int:id>', TipoUserView.as_view(), name='userstype.process'),
    path('directores/', DirectorView.as_view(), name="director_list"),
    path('directores/<int:id>', DirectorView.as_view(), name='director.process'),
    path('instituciones/', InstitucionView.as_view(), name="instituciones_list"),
    path('instituciones/<int:id>', InstitucionView.as_view(), name='instituciones.process'), 
    path('tutores/', TutorView.as_view(), name="tutores_list"),
    path('tutores/<int:id>', TutorView.as_view(), name='tutores.process')

]