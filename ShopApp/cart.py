from django.shortcuts import get_object_or_404
from .models import Phone, Customer
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

class Cart():
    def __init__(self, request):
        self.request = request
        self.cart = self.request.session.get('cart', {})

    def save(self):
        self.request.session['cart'] = self.cart  # Save cart to session
        self.request.session.modified = True
    
    def add(self, phone_id, quantity):
        phone_id = str(phone_id)
        if phone_id in self.cart:
            self.cart[phone_id]["quantity"] += quantity
        else:
            phone = get_object_or_404(Phone, id=phone_id)  # More robust retrieval
            discounted_price = phone.discounted_price()
            self.cart[phone_id] = {
                "quantity": quantity,
                "price": str(discounted_price),  # Store as string to avoid Decimal issues
                "name": phone.name,
                "image": phone.image.url,
                "discountPercentage": phone.discountPercentange  # Fixed typo
            }
        self.save()

    def remove(self, phone_id):
        phone_id = str(phone_id)
        if phone_id in self.cart:
            del self.cart[phone_id]
            self.save()

    def get_cart_items(self):
        cart_items = []
        for phone_id, item in self.cart.items():
            try:
                price = Decimal(str(item["price"]))  
                total_price = price * item["quantity"]
            except (InvalidOperation, TypeError, ValueError):
                total_price = Decimal("0.00")

            cart_items.append({
                "phone_id": phone_id,
                "name": item["name"],
                "image": item["image"],
                "price": item["price"],
                "quantity": item["quantity"],
                "total_price": str(total_price),  # Return as string for consistency
                # "discountPercentage": item["discountPercentange"]
            })
        return cart_items
    
    def get_total_price(self):
        try:
            return sum(Decimal(str(item["price"])) * item["quantity"] for item in self.cart.values())
        except InvalidOperation as e:
            print(f"Conversion error: {e}")
            return Decimal('0.00')
    
    def clear(self):
        self.request.session["cart"] = {}  # Fixed session usage
        self.request.session.modified = True
