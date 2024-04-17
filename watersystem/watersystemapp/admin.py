from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, LoginDetail, District, WaterProduct, Order, Address, OrderAddress

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name','last_name','role', 'date_joined')
    
    search_fields = ('username', 'email', 'first_name','last_name')
    ordering = ('-date_joined',)

# Register the custom admin class for your CustomUser model
admin.site.register(CustomUser, CustomUserAdmin)
# booking/admin.py


from django.contrib import admin
from .models import  VendorProduct, Cart, CartItem, OrderItem,ProductOrder

admin.site.register(LoginDetail)
admin.site.register(District)
admin.site.register(WaterProduct)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(OrderAddress)
admin.site.register(VendorProduct)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(ProductOrder)
admin.site.register(OrderItem)