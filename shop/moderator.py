from django.contrib import admin
import django.apps
from django.urls import path
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

models = django.apps.apps.get_models()

class showModeratorArea(admin.AdminSite):
    site_header = 'Moderator Area'

show_moderator_site = showModeratorArea(name='moderator panel')