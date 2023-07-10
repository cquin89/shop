from shop.models import *
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse

class ProductUtils:

    def createProduct(self,request,resultados):
     
        detalles_data = []
        for resultado in resultados:
            detalle_data = {
                'price': self.parseToFloat(resultado[2]),
                'store': resultado[4],
                'url': resultado[5],
                'nameStoreProduct':resultado[1]
            }
            detalles_data.append(detalle_data)
        
        print(f"Se obtuvieron todos los productos")

       
            # Obtener los detalles del producto

        productBrand = self.find_repeited_brand(resultados)
      
        primerProducto = resultados[0]
       # Crear el diccionario del producto
        producto_data = {
            'name':primerProducto[1],
            'pictureUrl': primerProducto[3],
            'brand': productBrand,
            'details': detalles_data
        }
        response_data = []
        response_data.append(producto_data)
        response = {
            'products': response_data
        }
        print(f"Se obtuvieron todos los productos")
        return JsonResponse(response)
        

    def find_repeited_brand(self,resultados):
        marcas = {}

        # Contar la frecuencia de las marcas en los resultados
        for resultado in resultados:
            marca = resultado[0]
            if marca in marcas:
                marcas[marca] += 1
            else:
                marcas[marca] = 1

        # Encontrar la marca más común
        marca_mas_comun = None
        max_frecuencia = 0
        for marca, frecuencia in marcas.items():
            if frecuencia > max_frecuencia:
                marca_mas_comun = marca
                max_frecuencia = frecuencia

        return marca_mas_comun
    
        
    def parseToFloat(self,cadena):
        cadena = cadena.replace(".", "").replace("$", "").replace(",", "").replace(" ", "")
        numero = float(cadena)
        return numero