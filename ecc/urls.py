# ecc/urls.py
from django.urls import path
from .views import ecc_input

urlpatterns = [
    path('', ecc_input, name='ecc_input'),
]
