from rest_framework import serializers
from .models import Usuario, Admin


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