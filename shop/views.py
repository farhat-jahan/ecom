from django.shortcuts import render

# Create your views here.

def index(request):
    """    Display website index-page
    :param request:
    :return:
    """
    return render(request, 'shop/index.html')