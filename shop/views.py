from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

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

    paginator = Paginator(prod_object, 1) #display 16 data/page
    print("paginator.num_pages to see total pages after pagination", paginator.num_pages)
    print("paginator.count to see total db product data before pagination", paginator.count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    prod_object = paginator.get_page(page_number)

    return render(request, 'shop/products.html', {'prod_object': prod_object, 'page_object': page_obj})
