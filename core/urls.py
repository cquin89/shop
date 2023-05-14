from django.contrib import admin
from django.urls import path, include

from shop.api.router import route_posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route_posts.urls)),
    path('', include('shop.urls'))
]

#admin.site.index_title = 'CarritoChek'
#admin.site.site_header = "CarritoChek"
#admin.site.site_title = "Admin panel"