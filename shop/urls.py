from django.contrib import admin
from django.urls import path
from . views import *
from django.conf.urls.static import static
from django.conf import settings


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
    path('mediatest/', media_url_test, name='media_test'),
#path('media/<str:file>', SecureMediaFile, name='media_file_secure'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
