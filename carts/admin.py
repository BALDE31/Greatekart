from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ()
    #prepopulated_fields = {'slug': ('product_name',)}

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ()
    #prepopulated_fields = {'slug': ('product_name',)}
