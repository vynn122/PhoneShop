from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Phone)
admin.site.register(Customer)
admin.site.register(Brand)
admin.site.register(Order)
admin.site.register(CartItem)