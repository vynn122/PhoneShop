from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def homepage(request):
    new_arrivals = Phone.objects.order_by('-created_at')[:12]
    iphone_phones = Phone.objects.filter(brand__name="Apple").order_by('-created_at')[:6]
    Samsung_phones = Phone.objects.filter(brand__name="SamSung").order_by('-created_at')[:6]
    Oppo_phones = Phone.objects.filter(brand__name="Oppo").order_by('-created_at')[:6]
    Vivo_phones = Phone.objects.filter(brand__name="Vivo").order_by('-created_at')[:6]
    context={
        "new_arri":new_arrivals,
        "iphone_phones": iphone_phones,
        "Samsung_phones": Samsung_phones,
        "Oppo_phones": Oppo_phones,
        "Vivo_phones": Vivo_phones,
    }
    return render(request,'ShopApp/index.html', context)

def loginpage(request):
    return render(request, 'ShopApp/components/login/login.html')


