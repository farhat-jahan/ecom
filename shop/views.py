from django.shortcuts import render
from .models import Product, Orders
from django.core.paginator import Paginator
from django.template import RequestContext

# Create your views here.

def index(request):
    """    Display website index-page
    :param request:
    :return:
    """
    return render(request, 'shop/index.html')

def home(request):
    """    Display website home-page
    :param request:
    :return:
    """
    return render(request, 'shop/home.html')

def about(request):
    """    Display website about-page
    :param request:
    :return:
    """
    return render(request, 'shop/about.html')


def display_products(request):
    prod_object = Product.objects.all()
    search_item = request.GET.get('item_name')

    if search_item != '' and search_item is not None:
        prod_object = Product.objects.filter(title__icontains=search_item)

    paginator = Paginator(prod_object, 2) #display 16 data/page
    print("paginator.num_pages to see total pages after pagination", paginator.num_pages)
    print("paginator.count to see total db product data before pagination", paginator.count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    prod_object = paginator.get_page(page_number)

    return render(request, 'shop/products.html', {'prod_object': prod_object, 'page_object': page_obj})


def display_product_details(request, prod_id):
    try:
        product_object = Product.objects.get(id=prod_id)
        print("product_object is empty or not----", product_object)
    except Exception as e:
        print("Exception in prod details--", e)
        product_object = []

    return render(request, "shop/product_details.html", {'product_object': product_object})


def checkout_products(request):
    if request.method == 'POST':
        item = request.POST.get('item', '')
        quantity = request.POST.get('quantity', '')
        price = request.POST.get('item-price', '')
        print("model--", price)
        name = request.POST.get('name','')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zipcode', '')
        order = Orders(item=item, quantity=quantity, price=price,name=name, email=email, address=address, city=city, state=state,zip_code=zip_code)
        order.save()
    return render(request,  "shop/checkout.html")#, RequestContext(request))


