from rest_framework import serializers
from .models import Categoria


class PruebaSerializer(serializers.Serializer):
    nombre= serializers.CharField(required=True)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categoria
        fields = '__all__'