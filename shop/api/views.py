from rest_framework.viewsets import ModelViewSet
from shop.api.serializers import *
from django.core.paginator import Paginator
from django.http import JsonResponse
from rest_framework.response import Response
from shop.models import *

class BrandApiViewSet(ModelViewSet):
    serializer_class = BrandSerilizer
    queryset = Brand.objects.all()

class ProductApiViewSet(ModelViewSet):
    serializer_class = ProductSerilizer
    queryset = Product.objects.all()

    def list(self, request, *args, **kwargs):
        print('pasando por get')
        nombre_producto = request.GET.get('nombre', '')  # Obtener el nombre del producto del parámetro de consulta 'nombre'
        nameCategory = request.GET.get('categoria', '')  # Obtener el ID de la categoría del parámetro de consulta 'categoria'

        # Filtrar productos por nombre y, opcionalmente, por categoría
        productos = Product.objects.filter(name__icontains=nombre_producto)
        category = Category.objects.filter(name__iexact=nameCategory).first()

        if category is not None:
            productos = productos.filter(category_id=category.id)
        
        # Crear un paginador con los productos encontrados
        paginator = Paginator(productos, 30)
        page_number = request.GET.get('page', 1)  # Obtener el número de página del parámetro de consulta 'page'
        page = paginator.get_page(page_number)

        # Obtener los productos de la página actual
        productos_pagina_actual = page.object_list

        # Crear una lista de diccionarios para almacenar los datos de cada producto
        response_data = []
        for producto in productos_pagina_actual:
            # Obtener los detalles del producto
            detalles_producto = ProductDetailt.objects.filter(product=producto)
            
            # Crear una lista de diccionarios para almacenar los datos de cada detalle
            detalles_data = []
            for detalle in detalles_producto:
                detalle_data = {
                    'price': detalle.price,
                    'storeId': detalle.store.id,
                    'storeName': detalle.store.name
                }
                detalles_data.append(detalle_data)
            
            # Crear el diccionario del producto
            producto_data = {
                'id': producto.id,
                'name': producto.name,
                'pictureUrl': producto.pictureUrl,
                'brand': producto.brand.name,
                'category': producto.category.name,
                'details': detalles_data
            }
            response_data.append(producto_data)

        # Crear un diccionario de respuesta que incluya los datos de los productos y la información de paginación
        response = {
            'total_pages': paginator.num_pages,
            'current_page': page_number,
            'products': response_data
        }

        return JsonResponse(response)

class CategoryApiViewSet(ModelViewSet):
    serializer_class = CategorySerilizer
    queryset = Category.objects.all()


class StoreApiViewSet(ModelViewSet):
    serializer_class = StoreSerilizer
    queryset = Store.objects.all()
