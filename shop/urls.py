from django.urls import path
from . import views

urlpatterns = [
    path('', views.redireccionar, name='getProduct'),
    path('moderator/getProduct', views.get_product, name='getProduct'),
    path('moderator/getProduct/getPrice', views.get_product_price, name='getProduct/getPrice'),
    path('moderator/unimarcTest', views.prueba_unimarc, name='unimarcTest'),
    path('moderator/jumboTest', views.prueba_jumbo, name='jumboTest'),
    path('moderator/santaIsabelTest', views.prueba_santa_isabel, name='santaIsabelTest'),
    path('moderator/liderTest', views.prueba_lider, name='liderTest')
    
]
