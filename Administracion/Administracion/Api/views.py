from django.shortcuts import render
from django.views import View
from .models import Usuario, Tipo_user, Director, Institucion, Tutor
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer

# Create your views here.

class JSONResponse(HttpResponse):

    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):

        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def users_list(request):

    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':

        usuarios = Usuario.objects.all()
        serializer = UserSerializer(usuarios, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)

        if serializer.is_valid():

            serializer.save()
            return JSONResponse(serializer.data, status=201)

        return JSONResponse(serializer.errors, status=400)

class TipoUserView(View): 

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        type = list(Tipo_user.objects.values())

        if len(type) > 0:

            datos = {'message': "Success", 'types': type}
        
        else: 
            
            datos = {'message': "Types of user not found"}

        return JsonResponse(datos)

    def post(self, request):

        jd = json.loads(request.body)
        Tipo_user.objects.create(tipo=jd['tipo'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):

        jd = json.loads(request.body)
        type = list(Tipo_user.objects.filter(id=id).values())

        if len(type) > 0: 

            type = Tipo_user.objects.get(id=id)
            type.tipo = jd['tipo']
            type.save()

        else: 

            datos = {'message': "Success"}

        return JsonResponse(datos)

    def delete(self, request, id):

        type = list(Tipo_user.objects.filter(id=id).values())

        if len(type) > 0:

            Tipo_user.objects.filter(id=id).delete()

        else: 

            datos = {'message': "Tipos de usuarios no encontradas"}

        return JsonResponse(datos)

class DirectorView(View): 

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        director = list(Director.objects.values())

        if len(director) > 0:

            datos = {'message': "Success", 'director': director}
        
        else: 
            
            datos = {'message': "Director not found"}

        return JsonResponse(datos)

    def post(self, request):

        jd = json.loads(request.body)
        Director.objects.create(nombres=jd['nombres'], apellidos=jd['apellidos'], dni=jd['dni'], email=jd['email'], telefono=jd['telefono'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):

        jd = json.loads(request.body)
        director = list(Director.objects.filter(id=id).values())

        if len(director) > 0: 

            director = Director.objects.get(id=id)
            director.nombres = jd['nombres']
            director.apellidos = jd['apellidos']
            director.dni = jd['dni']
            director.email = jd['email']
            director.telefono = jd['telefono']
            director.save()

        else: 

            datos = {'message': "Success"}

        return JsonResponse(datos)

    def delete(self, request, id):

        director = list(Director.objects.filter(id=id).values())

        if len(director) > 0:

            Director.objects.filter(id=id).delete()

        else: 

            datos = {'message': "Directores no encontrados"}

        return JsonResponse(datos)


class InstitucionView(View): 

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        institucion = list(Institucion.objects.values())

        if len(institucion) > 0:

            datos = {'message': "Success", 'institucion': institucion}
        
        else: 
            
            datos = {'message': "institucion not found"}

        return JsonResponse(datos)

    def post(self, request):

        jd = json.loads(request.body)
        Institucion.objects.create(nombre=jd['nombre'], director=jd['director'], cod_modular=jd['cod_modular'], cod_local=jd['cod_local'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):

        jd = json.loads(request.body)
        institucion = list(Institucion.objects.filter(id=id).values())

        if len(institucion) > 0: 

            institucion = Director.objects.get(id=id)
            institucion.nombre = jd['nombre']
            institucion.director = jd['director']
            institucion.cod_modular = jd['cod_modular']
            institucion.cod_local = jd['cod_local']
            institucion.save()

        else: 

            datos = {'message': "Success"}

        return JsonResponse(datos)

    def delete(self, request, id):

        institucion = list(Institucion.objects.filter(id=id).values())

        if len(institucion) > 0:

            Institucion.objects.filter(id=id).delete()

        else: 

            datos = {'message': "institucion no encontrados"}

        return JsonResponse(datos)

class TutorView(View): 

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        tutor = list(Tutor.objects.values())

        if len(tutor) > 0:

            datos = {'message': "Success", 'tutor': tutor}
        
        else: 
            
            datos = {'message': "Tutor not found"}

        return JsonResponse(datos)

    def post(self, request):

        jd = json.loads(request.body)
        Tutor.objects.create(nombres=jd['nombres'], apellidos=jd['apellidos'], fecha_nac=jd['fecha_nac'], dni=jd['dni'], email=jd['email'], password=jd['password'], telefono=jd['telefono'], institucion=jd['institucion'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):

        jd = json.loads(request.body)
        tutor = list(Tutor.objects.filter(id=id).values())

        if len(tutor) > 0: 

            tutor = Director.objects.get(id=id)
            tutor.nombres = jd['nombres']
            tutor.apellidos = jd['apellidos']
            tutor.fecha_nac = jd['fecha_nac']
            tutor.dni = jd['dni']
            tutor.password = jd['password']
            tutor.telefono = jd['telefono']
            tutor.institucion = jd['institucion']
            tutor.save()

        else: 

            datos = {'message': "Success"}

        return JsonResponse(datos)

    def delete(self, request, id):

        tutor = list(Tutor.objects.filter(id=id).values())

        if len(tutor) > 0:

            Tutor.objects.filter(id=id).delete()

        else: 

            datos = {'message': "tutor no encontrados"}

        return JsonResponse(datos)
