from django.contrib import admin
from shop.models import Brand
from shop.models import Product
from shop.models import Category
from shop.models import Store
from shop.models import ProductDetailt
from django.urls import path
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

@admin.register(Brand)
class addBrand(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Category)
class addStore(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Store)
class addCategory(admin.ModelAdmin):
    list_display = ['name']

    
@admin.register(Product)
class addProduct(admin.ModelAdmin):
    list_display = ['name','get_brand_name','get_category_name']

    @admin.display(description='Brand Name', ordering='brand__name')
    def get_brand_name(self, obj):
        return obj.brand.name

    @admin.display(description='Category Name', ordering='category__name')
    def get_category_name(self, obj):
        return obj.category.name
    
@admin.register(ProductDetailt)
class addProductDetailt(admin.ModelAdmin):
    list_display = ['nameStoreProduct','price','url','get_store_name','get_product_name']

    @admin.display(description='Store Name', ordering='store__name')
    def get_store_name(self, obj):
        return obj.store.name

    @admin.display(description='Product Name', ordering='product__name')
    def get_product_name(self, obj):
        return obj.product.name
    