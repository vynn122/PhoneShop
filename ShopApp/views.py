from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.utils.timezone import now
from datetime import timedelta
from django.views.decorators.cache import never_cache
from django.contrib.messages import get_messages

# Create your views here.
def homepage(request): 
    new_arrivals = Phone.objects.order_by('-created_at')[:12]
    iphone_phones = Phone.objects.filter(brand__name="Apple").order_by('-created_at')[:6]
    Samsung_phones = Phone.objects.filter(brand__name="SamSung").order_by('-created_at')[:6]
    Oppo_phones = Phone.objects.filter(brand__name="Oppo").order_by('-created_at')[:6]
    Vivo_phones = Phone.objects.filter(brand__name="Vivo").order_by('-created_at')[:6]
    customer = Customer.objects.filter(id=request.session.get("customer_id")).first()
    if not customer:
        customer = Customer.objects.filter(name="Guest").first()
    cart = Cart.objects.filter(customer_name=customer).first()
    cart_items = cart.items.all() if cart else []

    cart = Cart.objects.filter(customer_name=customer).first()
    cart_items = cart.items.all() if cart else []
    context={
        "new_arri":new_arrivals,
        "iphone_phones": iphone_phones,
        "Samsung_phones": Samsung_phones,
        "Oppo_phones": Oppo_phones,
        "Vivo_phones": Vivo_phones,
        "cart_items": cart_items,
        "customer": customer,
    }
    return render(request,'ShopApp/index.html', context)
def all_phones(request):
    all_phones = Phone.objects.all()
    iphone_phones = Phone.objects.filter(brand__name="Apple")
    Samsung_phones = Phone.objects.filter(brand__name="SamSung")
    Oppo_phones = Phone.objects.filter(brand__name="Oppo")
    Vivo_phones = Phone.objects.filter(brand__name="Vivo")
    customer = Customer.objects.filter(id=request.session.get("customer_id")).first()
    if not customer:
        customer = Customer.objects.filter(name="Guest").first()
    context = {
        "customer": customer,
        "all_phones": all_phones,
        "iphone_phones": iphone_phones,
        "Samsung_phones": Samsung_phones,
        "Oppo_phones": Oppo_phones,
        "Vivo_phones": Vivo_phones,
    }
    return render(request, 'ShopApp/components/product/all_phones.html', context)
def brand_iphone(request):
    iphone_phones = Phone.objects.filter(brand__name="Apple")
    customer = Customer.objects.filter(id=request.session.get("customer_id")).first()
    if not customer:
        customer = Customer.objects.filter(name="Guest").first()
    context = {
        "customer": customer,
        "iphone_phones": iphone_phones,
    }
    return render(request, 'ShopApp/components/product/iphone.html', context)
def brand_samsung(request):
    Samsung_phones = Phone.objects.filter(brand__name="SamSung")
    customer = Customer.objects.filter(id=request.session.get("customer_id")).first()
    if not customer:
        customer = Customer.objects.filter(name="Guest").first() 
    context = {
        "customer": customer,
        "Samsung_phones": Samsung_phones,
    }
    return render(request, 'ShopApp/components/product/ss.html', context)

def brand_oppo(request):
    Oppo_phones = Phone.objects.filter(brand__name="Oppo")
    customer = Customer.objects.filter(id=request.session.get("customer_id")).first()
    if not customer:
        customer = Customer.objects.filter(name="Guest").first() 
    context = {
        "customer": customer,
        "Oppo_phones": Oppo_phones,
    }
    return render(request, 'ShopApp/components/product/oppo.html', context)

def brand_vivo(request):
    Vivo_phones = Phone.objects.filter(brand__name="Vivo")
    customer = Customer.objects.filter(id=request.session.get("customer_id")).first()
    if not customer:
        customer = Customer.objects.filter(name="Guest").first() 
    context = {
        "customer": customer,
        "Vivo_phones": Vivo_phones,
    }
    return render(request, 'ShopApp/components/product/vivo.html', context)

def single_product(request, product_id):
    product = get_object_or_404(Phone, id=product_id)
    customer = Customer.objects.filter(id=request.session.get("customer_id")).first()
    if not customer:
        customer = Customer.objects.filter(name="Guest").first()

    context = {
        "product": product,
        "customer": customer,
    }
    return render(request, "ShopApp/components/product/single_product.html", context)





def about(request):
    customer = Customer.objects.filter(id=request.session.get("customer_id")).first()
    if not customer:
        customer = Customer.objects.filter(name="Guest").first()
    return render(request, 'ShopApp/components/aboutUs/about.html', {"customer": customer})





# register
def register_customer(request):
    storage = get_messages(request)
    for _ in storage:
        pass  # This clears the stored messages

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]

        if Customer.objects.filter(email=email).exists():
            print(f"Email already exists: {email}")             
            messages.error(request, "Email already exists!")
            return render(request, "ShopApp/components/login/register.html", {"error": "Email already exists!"})
       
        hashed_password = make_password(password)
        customer = Customer(name=name, email=email, password=hashed_password)
        customer.save()
        
        messages.success(request, "Account created successfully! And you can login now🥱😴")
        # return redirect("loginpage") 

    return render(request, "ShopApp/components/login/register.html")

# login
@csrf_protect
def login_customer(request):
    if request.method == "POST":
        email = request.POST["phone_or_email"]
        password = request.POST["password"]

        try:
            customer = Customer.objects.get(email=email)
            if customer.check_password(password): 
                request.session["customer_id"] = customer.id  
                request.session["customer_name"] = customer.name
                #use this to set session expire in 30 minutes
                request.session.set_expiry(timedelta(minutes=30))
                messages.success(request, f"Login successful! Welcome back bro {customer.name} 💩")
                # return redirect("homepage")
            else:
                messages.error(request, "Invalid password! Please try again. Khos password hz bro!!") 
                return redirect("loginpage") 
                # return render(request, "ShopApp/components/login/login.html", {"error": "Invalid password!"})
        except Customer.DoesNotExist:
            messages.error(request, "Job hz bro, bro not yet our customer!! Please register first.")
            redirect("register")
            # return render(request, "ShopApp/components/login/login.html", {"error": "Customer not found!"})

    return render(request, "ShopApp/components/login/login.html")
# logout    
@never_cache
def logout_customer(request):
    logout(request)
    request.session.flush()
    return redirect('homepage')


