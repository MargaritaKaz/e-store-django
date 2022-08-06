from django.contrib import admin
from .models import Brand, Operating_system, Processor, Promocode, Computer, Order, Manager, OrderDetail, Cart, CartItem, Order_status
# Register your models here.
admin.site.register(Brand)
admin.site.register(Operating_system)
admin.site.register(Processor)
admin.site.register(Promocode)
admin.site.register(Computer)
admin.site.register(Order)
admin.site.register(Manager)
admin.site.register(OrderDetail)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order_status)




class CartInline(admin.TabularInline):
    model = Cart

class CartAdmin(admin.ModelAdmin):
    inlines = [CartInline,]

class ComputerAdmin(admin.ModelAdmin):
    inlines = [CartInline,]    

# cart
class CartAdmin(admin.ModelAdmin):
    pass

class CartItemAdmin(admin.ModelAdmin):
    pass    