from rest_framework import serializers
from .models import Usuario


class UserSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    nombres = serializers.CharField()
    apellidos = serializers.CharField()
    fecha_nac = serializers.DateField()
    dni = serializers.CharField()
    correo = serializers.EmailField()
    password = serializers.CharField()
    telefono = serializers.CharField()
    tipo = serializers.CharField()
    institucion = serializers.CharField()
    tutor = serializers.CharField()

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
        instance.fecha_nac = validated_data.get('fecha_nac', instance.fecha_nac)
        instance.dni = validated_data.get('dni', instance.dni)
        instance.correo = validated_data.get('correo', instance.correo)
        instance.password = validated_data.get('password', instance.password)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.institucion = validated_data.get('institucion', instance.institucion)
        instance.tutor = validated_data.get('tutor', instance.tutor)
        instance.save()
        return instance

    class Meta:
        model = Usuario
        fields = ('nombres', 'apellidos', 'fecha_nac', 'dni', 'correo', 'password', 'telefono', 'tipo', 'institucion', 'tutor')