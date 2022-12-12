from rest_framework import serializers
from .models import Usuario, Admin, Reporte

class UserSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    nombres = serializers.CharField()
    apellidos = serializers.CharField()
    dni = serializers.CharField()
    correo = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):

        """
        Create and return a new `Serie` instance, given the validated data.
        """
        return Usuario.objects.create(**validated_data)

    def update(self, instance, validated_data):

        """
        Update and return an existing `Serie` instance, given the validated data.
        """
        instance.nombres = validated_data.get('nombres', instance.nombres)
        instance.apellidos = validated_data.get('apellidos', instance.apellidos)
        instance.dni = validated_data.get('dni', instance.dni)
        instance.correo = validated_data.get('correo', instance.correo)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

    class Meta:
        model = Usuario
        fields = ('nombres', 'apellidos', 'dni', 'correo', 'password')

class ReporteSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    filename = serializers.CharField()
    id_usuario = serializers.CharField()
    fecha_emitido = serializers.DateTimeField()
    estado = serializers.CharField()

    def create(self, validated_data):
        return Reporte.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.filename = validated_data.get('filename', instance.filename)
        instance.id_usuario = validated_data.get('filename', instance.id_usuario)
        instance.fecha_emitido = validated_data.get('filename', instance.fecha_emitido)
        instance.estado = validated_data.get('filename', instance.estado)
        instance.save()
        return instance
        
    class Meta:
        model = Reporte
        fields = ('filename', 'id_usuario', 'fecha_emitido', 'estado')

class AdminSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    nombres = serializers.CharField()
    apellidos = serializers.CharField()
    dni = serializers.CharField()
    correo = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):

        """
        Create and return a new `Serie` instance, given the validated data.
        """
        return Admin.objects.create(**validated_data)

    def update(self, instance, validated_data):

        """
        Update and return an existing `Serie` instance, given the validated data.
        """
        instance.nombres = validated_data.get('nombres', instance.nombres)
        instance.apellidos = validated_data.get('apellidos', instance.apellidos)
        instance.dni = validated_data.get('dni', instance.dni)
        instance.correo = validated_data.get('correo', instance.correo)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

    class Meta:
        model = Admin
        fields = ('nombres', 'apellidos', 'dni', 'correo', 'password')