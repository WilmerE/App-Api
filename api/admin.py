from django.contrib import admin
from api.models import Articulo

# Register your models here.
#admin.site.register(Articulo)

@admin.register(Articulo)

class ArticuloModel(admin.ModelAdmin):
	list_filter = ('titulo', 'descripcion')
	list_display = ('titulo', 'descripcion')