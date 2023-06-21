from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id','slug')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'id','user', 'category', 'stars')


@admin.register(ProductImg)
class ProductImgAdmin(admin.ModelAdmin):
    list_display = ('product', 'id')



@admin.register(SizeLetter)
class SizeLetterAdmin(admin.ModelAdmin):
    list_display = ('product','id', 'size','stok')


@admin.register(ProductStok)
class ProductStokAdmin(admin.ModelAdmin):
    list_display = ('product','id')

@admin.register(Gander)
class GanderAdmin(admin.ModelAdmin):
    list_display = ('title','id')
    
@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    
@admin.register(ProductTuru)
class ProductTuruAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','id')
    
@admin.register(ShopBasket)
class ShopBasketAdmin(admin.ModelAdmin):
    list_display = ('user', "sizeletter", "price_all", "count", 'id')

admin.site.register(Comment)
admin.site.register(Contact)