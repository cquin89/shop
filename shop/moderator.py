from django.contrib import admin
import django.apps
from shop.models import Brand
from shop.models import Product
from shop.models import Category
from shop.models import Store
from shop.models import ProductDetailt
from django.urls import path
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

models = django.apps.apps.get_models()

class showModeratorArea(admin.AdminSite):
    site_header = 'Moderator Area'

show_moderator_site = showModeratorArea(name='moderator panel')

show_moderator_site.register(Brand)
class addBrand(admin.ModelAdmin):
    list_display = ['name']