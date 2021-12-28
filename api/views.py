from django.shortcuts import render, HttpResponse, get_object_or_404
#from django.views.decorators.csrf import csrf_exempt
from api.models import Articulo
from api.serializers import ArticuloSerializer
#from django.http import JsonResponse
#from rest_framework.parsers import JSONParser
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#from rest_framework.decorators import APIView

#from rest_framework import generics
from rest_framework import mixins

from rest_framework import viewsets

# Create your views here.
def Index(request):
	return HttpResponse("Funcionando")

class ArticuloViewSet(viewsets.ModelViewSet):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloSerializer

"""
class ArticuloViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
					mixins.CreateModelMixin, mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin, mixins.DestroyModelMixin):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloSerializer
"""

"""
class ArticuloViewSet(viewsets.ViewSet):

	def list(self, request):
		articulos = Articulo.objects.all()
		serializer = ArticuloSerializer(articulos, many=True)
		return Response(serializer.data)

	def create(selsef, request):
		serializer = ArticuloSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def retrieve(self, request, pk=None):
		queryset = Articulo.objects.all()
		articulo = get_object_or_404(queryset, pk=pk)
		serializer = ArticuloSerializer(articulo)
		return Response(serializer.data)

	def update(self, request, pk=None):
		articulo = Articulo.objects.get(pk=pk)
		serializer = ArticuloSerializer(articulo, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def destroy(self, request, pk=None):
		articulo = Articulo.objects.get(pk=pk)
		articulo.delete
		return Response(status=status.HTTP_204_NO_CONTENT)
"""

"""
class ArticuloList(generics.GenericAPIView,
				mixins.ListModelMixin,
				mixins.CreateModelMixin):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request)

	def post(self, request, *args, **kwargs):
		return self.create(request)

class ArticuloDetalle(generics.GenericAPIView, mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin, mixins.DestroyModelMixin):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloSerializer

	lookup_field = 'id'

	def get(self, request, id):
		return self.retrieve(request, id=id)

	def put(self, request, id):
		return self.update(request, id=id)

	def delete(self, request, id):
		return self.destroy(request, id=id)
"""


"""
class ArticuloList(APIView):

	def get(self, request):
		articulos = Articulo.objects.all()
		serializer = ArticuloSerializer(articulos, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ArticuloSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticuloDetalle(APIView):

	def get_object(self, id):
		try:
			return Articulo.objects.get(id=id)
		except Articulo.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

	def get(self, request, id):
		articulo = self.get_object(id)
		serializer = ArticuloSerializer(articulo)
		return Response(serializer.data)

	def put(self, request, id):
		articulo = self.get_object(id)
		serializer = ArticuloSerializer(articulo, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, id):
		articulo = self.get_object(id)
		articulo.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
"""


"""
#@csrf_exempt
@api_view(['GET', 'POST'])
def articulo_lista(request):
	if request.method == 'GET':
		articulos = Articulo.objects.all()
		serializer = ArticuloSerializer(articulos, many=True)
		#return JsonResponse(serializer.data, safe=False)
		return Response(serializer.data)

	elif request.method == 'POST':
		#data = JSONParser().parse(request)
		serializer = ArticuloSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			#return JsonResponse(serializer.data, status=201)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		#return JsonResponse(serializer.errors, status=400)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def articulo_detalle(request, pk):
	try:
		articulo = Articulo.objects.get(pk=pk)
	except Articulo.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = ArticuloSerializer(articulo)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = ArticuloSerializer(articulo, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		articulo.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
"""