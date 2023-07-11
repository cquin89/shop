from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls'))
]

#admin.site.index_title = 'CarritoChek'
#admin.site.site_header = "CarritoChek"
#admin.site.site_title = "Admin panel"