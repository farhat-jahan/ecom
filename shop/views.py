from django.shortcuts import render
from .models import Product
# Create your views here.

def index(request):
    """    Display website index-page
    :param request:
    :return:
    """
    return render(request, 'shop/index.html')


def display_product(request):
    prod_object = Product.objects.all()
    search_item = request.GET.get('item_name')

    if search_item != '' and search_item is not None:
        prod_object = Product.objects.filter(title__icontains=search_item)

    return render(request, 'shop/products.html', {'prod_object': prod_object})