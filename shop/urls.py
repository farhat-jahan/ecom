from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [
   # path('product/', admin.site.urls),
    path('index/', index, name='index')
]
