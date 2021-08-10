from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [
   # path('product/', admin.site.urls),
    path('index/', index, name='index'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('signin/', sign_in, name='signin'),
    path('signup/', sign_up, name='signup'),
    path('feedback/', feedback, name='feedback'),
    path('sendemail/', send_email, name='send_email'),
    path('product/', display_products, name='display_products'),
    path('product/<int:prod_id>/', display_product_details, name='display_product_details'),
    path('checkout/', checkout_products, name='checkout_products'),
]
