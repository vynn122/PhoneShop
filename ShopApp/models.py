from django.db import models
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Phone(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discountPercentange = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="phones")

    def __str__(self):
        return f"{self.name} ({self.brand.name})"
    @property
    def discounted_price(self):
        """
        Returns the price after applying the discount percentage.
        """
        if self.discountPercentange:  
            discount_amount = (self.discountPercentange / 100) * self.price
            return self.price - discount_amount
        return self.price
    
class Customer(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(unique=True  ,null=True)  
    password = models.CharField(max_length=200) 

    def set_password(self, raw_password):
        """Hashes the password and sets it"""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Checks if the provided password matches the stored hashed password"""
        return check_password(raw_password, self.password)
    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    phone = models.ForeignKey('Phone', on_delete=models.CASCADE, related_name="orders")
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(default=now)

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"

    @property
    def total_price(self):
        return self.phone.price * self.quantity


class Role(models.Model):
    role_name = models.CharField(max_length=200, unique=True)

class Employee(models.Model):
    employee_name = models.CharField(max_length=200)
    employee_role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="roles")


class Cart(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)