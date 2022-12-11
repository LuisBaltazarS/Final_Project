from .models import Usuario, Admin
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer, AdminSerializer

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

@csrf_exempt
def admin_list(request):

    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':

        administradores = Admin.objects.all()
        serializer = AdminSerializer(administradores, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = AdminSerializer(data=data)

        if serializer.is_valid():

            serializer.save()
            return JSONResponse(serializer.data, status=201)

        return JSONResponse(serializer.errors, status=400)

