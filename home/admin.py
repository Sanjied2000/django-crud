from django.contrib import admin
from home.models import Shop

# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id','ShopName', 'Address', 'Phone') 
    search_fields = ('ShopName', 'Phone') 
admin.site.register(Shop, ShopAdmin)

from .models import Fruit

class FruitAdmin(admin.ModelAdmin):
    list_display = ('fruit_name', 'price', 'shop')  
    search_fields = ('fruit_name',)  
    list_filter = ('shop',)  

admin.site.register(Fruit, FruitAdmin)

from .models import AdminShop

class AdminShopAdmin(admin.ModelAdmin):
    list_display = ('user', 'shop')  # Displays user and shop in the list view
    
    list_filter = ('shop','user')  # Adds filtering options by shop in the sidebar

admin.site.register(AdminShop, AdminShopAdmin)