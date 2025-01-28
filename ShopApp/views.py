from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def homepage(request):
    new_arrivals = Phone.objects.order_by('-created_at')[:6]
    return render(request,'ShopApp/index.html', context={"new_arri":new_arrivals })

def loginpage(request):
    return render(request, 'ShopApp/components/login/login.html')


def samsung_brand(request):
    brand_name = "Samsung"  
    brand = get_object_or_404(Brand, name=brand_name)
    phones = brand.phones.all() 
    return render(request, 'specific_brand.html', {'brand': brand, 'phones': phones})