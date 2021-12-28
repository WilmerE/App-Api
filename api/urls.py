from django.urls import path
from api.views import (Index,)

app_name = 'urls'

urlpatterns = [
	path('', Index, name='index'),
]