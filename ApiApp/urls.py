from django.contrib import admin
from django.urls import path, include
#from api.views import articulo_lista, articulo_detalle
#from api.views import ArticuloList, ArticuloDetalle
from rest_framework.routers import DefaultRouter
from api.views import ArticuloViewSet

router = DefaultRouter()
router.register('articulos', ArticuloViewSet, basename='articulos')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('articulo/', articulo_lista),
    #path('articulo/<int:pk>', articulo_detalle),
    #path('articulo/', ArticuloList.as_view()),
    #path('articulo/<int:id>', ArticuloDetalle.as_view()),
    path('', include(router.urls)),
    path('', include('api.urls', namespace='urls_api'))
]
