from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

    
class ShopAdminArea(admin.AdminSite):
    site_header = 'Admin Area'

shop_admin_site = ShopAdminArea(name='BlogAdmin')