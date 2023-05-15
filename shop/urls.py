from django.urls import path
from . import views

urlpatterns = [
    path('', views.redireccionar, name='addProduct'),
    path('moderator/addProduct', views.mi_formulario, name='addProduct')
]
