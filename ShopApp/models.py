from django.db import models
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password, check_password
from decimal import Decimal, ROUND_HALF_UP
# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Phone(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    DISCOUNT_CHOICES = [
        (0, '0%'), 
        (5, '5%'),
        (10, '10%'),
        (15, '15%'),
        (20, '20%'),
        (25, '25%'),
        (50, '50%'),
        (75, '75%'),
        (100, '100%'),  
    ]
    # discountPercentange = models.IntegerField(default=0)
    discountPercentange = models.IntegerField(choices=DISCOUNT_CHOICES, default=0)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="phones")

    def __str__(self):
        return f"{self.name} ({self.brand.name})"
    def discounted_price(self):
        """
        ❓Why this method is used?:
        This returns the price after applying the discount percentage, formatted to two decimal places.
        """
        discount_amount = (Decimal(self.discountPercentange) / Decimal(100)) * self.price
        discounted_price = self.price - discount_amount
        #  Note!!:  ❓ in here we use the quantize method to round the discounted price to two decimal places❓
        #  Note!!:  ❓ the rounding method ROUND_HALF_UP is used to round the decimal number that ends in 5 or higher rounds up to the next decimal place.❓
        return discounted_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)



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
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Order {self.id} by {self.customer.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity} x {self.phone.name}"


class Role(models.Model):
    role_name = models.CharField(max_length=200, unique=True)

class Employee(models.Model):
    employee_name = models.CharField(max_length=200)
    employee_role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="roles")
