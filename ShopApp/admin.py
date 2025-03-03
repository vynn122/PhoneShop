from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Phone)
admin.site.register(Customer)
admin.site.register(Brand)
admin.site.register(CartItem)



class TransactionAdmin(admin.ModelAdmin):
    list_display=('id', 'phone', 'brand', 'quantity', 'total_price', 'customer', 'ordered_at')
admin.site.register(Transaction, TransactionAdmin)