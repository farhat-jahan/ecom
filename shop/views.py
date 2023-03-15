import os.path

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Orders, MediaTest
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import FileResponse
from django.views.defaults import page_not_found
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    """    Display website index-page
    :param request:
    :return:
    """
    #return render(request, 'shop/index.html')
    data = Product.objects.all()
    return render(request, 'shop/index.html',{'data':data})



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


@csrf_exempt
def sign_in(request):
    """    Display website sign-in-page
    :param request:
    :return:
    """
    username = ''
    user_password = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        
        if user is None:
            username = 'Username not found, Try again'
            user_password = 'Password not found, Try again'
        else:
            login(request, user)
            return redirect('/shop/product')

    return render(request, 'shop/signin.html', {'username': username, 'user_password': user_password})


@csrf_exempt
def sign_up(request):
    """    Display website sign-in-page
    :param request:
    :return:
    """
    error = ''
    usernameexist = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        user = authenticate(username=username, password=password)

        if password != confirmpassword:
            error = 'Password and confirm password are mismatched'
            return render(request, 'shop/signup.html', {'error': error})
        if user is None:
            new_user = User(username=username)
            new_user.save()
            new_user.set_password(password)
            new_user.save()
            return redirect('/shop/product')

    return render(request, 'shop/signup.html')


def display_products(request):
    prod_object = Product.objects.all()
    search_item = request.GET.get('item_name')

    if search_item != '' and search_item is not None:
        prod_object = Product.objects.filter(title__icontains=search_item)

    paginator = Paginator(prod_object, 2)  # display 16 data/page
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
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zipcode', '')
        order = Orders(item=item, quantity=quantity, price=price, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code)
        order.save()
    return render(request, "shop/checkout.html")  # , RequestContext(request))


# TODO: need to implement this
def send_email(request):
    """    Display website send email-page
    :param request:
    :return:
    """
    if request.method == 'POST':
        pass
    return render(request, 'shop/sendemail.html')


# TODO: need to implement this
@csrf_exempt
def feedback(request):
    """    Display website feedback
    :param request:
    :return:
    """
    print("hi@@@@ ", request.POST)
    if request.method == 'POST':
        message = request.POST.get['msg']
        print("hiiii", message)
        pass
    return render(request, 'shop/sendemail.html')

def media_url_test(request):
    """URL: http://127.0.0.1:8000/shop/mediatest/
    note:SecureMediaFile method will protect to open media file based on login
    """
    data = MediaTest.objects.all().last()
    return render(request,'shop/media_test.html',{'data':data})

@login_required
def SecureMediaFile(request, file):
    """This protects opening of media file, werever it is used."""
    print("Executing SecureMediaFile...")
    data = get_object_or_404(MediaTest)
    print(data)
    path, file_name = os.path.split(file)
    response = FileResponse(data.image_details)
    return response
