from django.urls import path
from apps.inicio.views import *

app_name='inicio'

urlpatterns = [
    path('inicio/', inicio,name='inicio')
]
