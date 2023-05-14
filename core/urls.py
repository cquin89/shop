from django.contrib import admin
from django.urls import path, include
from shop.admin import shop_admin_site

from shop.api.router import route_posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/test', shop_admin_site.urls),
    path('api/', include(route_posts.urls)),
]

#admin.site.index_title = 'CarritoChek'
#admin.site.site_header = "CarritoChek"
#admin.site.site_title = "Admin panel"