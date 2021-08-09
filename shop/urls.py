from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [
   # path('product/', admin.site.urls),
    path('index/', index, name='index'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('product/', display_products, name='display_products'),
    path('product/<int:prod_id>/', display_product_details, name='display_product_details'),
    path('checkout/', checkout_products, name='checkout_products'),
]
