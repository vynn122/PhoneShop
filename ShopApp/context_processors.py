from .models import CartItem, Customer

def cart_context(request):
    customer = Customer.objects.filter(id=request.session.get("customer_id")).first()
    
    if customer:
        cart_items = CartItem.objects.filter(customer=customer)
        total_price = sum(item.total_price() for item in cart_items)  
        cart_count = cart_items.count()
        cart_quantity = sum(item.quantity for item in cart_items) 
    else:
        cart_items = []
        total_price = 0
        cart_count = 0
        cart_quantity =0

    return {
        "cart_items": cart_items,
        "cart_total": total_price,
        "cart_count": cart_count,
        "cart_quantity": cart_quantity,
    }
