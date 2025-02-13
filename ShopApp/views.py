from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.utils.timezone import now
from datetime import timedelta
from django.views.decorators.cache import never_cache
from django.contrib.messages import get_messages
# from ...test.work.moha_work.utils import *
import json
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


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
    customer_id = request.session.get("customer_id")
    customer = None
    print(customer)
    if customer_id:
        customer = Customer.objects.filter(id=customer_id).first()
    context={
        "new_arri":new_arrivals,
        "iphone_phones": iphone_phones,
        "Samsung_phones": Samsung_phones,
        "Oppo_phones": Oppo_phones,
        "Vivo_phones": Vivo_phones,
        # "cart_items": cart_items,
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
    # if not customer:
    #     customer = Customer.objects.filter(name="Guest").first()
    customer_id = request.session.get("customer_id")
    customer = None
    print(customer)
    if customer_id:
        customer = Customer.objects.filter(id=customer_id).first()
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
                request.session.set_expiry(timedelta(minutes=130))
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

# create login required decorator
def login_required(view_func):
    """Custom login required decorator for session-based authentication."""
    def wrapper(request, *args, **kwargs):
        if 'customer_id' not in request.session:
            messages.error(request, "You need to log in to continue!")
            return redirect("loginpage")
        return view_func(request, *args, **kwargs)
    return wrapper


@login_required
def updateItem(request):
    if request.method != "POST":
        return JsonResponse({'error': 'Invalid request method'}, status=400)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    productId = data.get('productId')
    action = data.get('action')

    if not productId or not action:
        return JsonResponse({'error': 'Missing productId or action'}, status=400)

    print('Action:', action)
    print('Product:', productId)

    customer = Customer.objects.filter(id=request.session.get("customer_id")).first()
    product = Phone.objects.filter(id=productId).first()

    if not product:
        return JsonResponse({'error': 'Product not found'}, status=404)

    cart, created = CartItem.objects.get_or_create(customer=customer, phone=product)
    

    if action == 'add':
        cart.quantity += 1
    elif action == 'remove':
        cart.quantity -= 1

    if cart.quantity <= 0:
        cart.delete()
    else:
        cart.save()
        # test
    cart_items = CartItem.objects.filter(customer=customer)
    cart_total = sum(item.phone.discounted_price() * item.quantity for item in cart_items)
    cart_count = cart_items.count()
    cart_quantity = sum(item.quantity for item in cart_items) 

    cart_items_list = [
        {
            'id': item.phone.id,
            'name': item.phone.name,
            'image': item.phone.image.url if item.phone.image else '',
            'price': item.phone.discounted_price(),
            'quantity': item.quantity,
        }
        for item in cart_items
    ]
    
    return JsonResponse({
        'message': 'Item updated',
        'cart_items': cart_items_list,
        'cart_total': cart_total,
        'cart_quantity' : cart_quantity,
    })

    return JsonResponse({'message': 'Item updated', 'quantity': cart.quantity}, safe=False)



