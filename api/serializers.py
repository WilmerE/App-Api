from rest_framework import serializers
from api.models import Articulo

"""
class ArticuloSerializer(serializers.Serializer):
	titulo = serializers.CharField(max_length=100)
	descripcion = serializers.CharField(max_length=400)

	def create(self, validated_data):
		return Articulo.objects.create(validated_data)

	def update(self, instance, validated_data):
		instance.titulo = validated_data.get('titulo', instance.titulo)
		instance.descripcion = validated_data.get('descripcion', instance.descripcion)
"""
class ArticuloSerializer(serializers.ModelSerializer):
	class Meta:
		model = Articulo
		fields = ['id', 'titulo', 'descripcion']
