from django.urls import path
from authapp.views import *

urlpatterns = [
    path('', Home, name='Home')
]