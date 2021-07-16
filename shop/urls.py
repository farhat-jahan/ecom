from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [
   # path('product/', admin.site.urls),
    path('index/', index, name='index'),
    path('product/', display_products, name='display_products'),
    path('product/<int:prod_id>/', display_product_details, name='display_product_details')
]
