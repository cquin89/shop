from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from shop.utils.ScrapingUtil import ScrappingUtil
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponseBadRequest
from shop.scraping.scrapping_unimarc import *
from shop.scraping.scrapping_jumbo import *
from shop.scraping.scrapping_lider import *
from shop.scraping.scrapping_santaisabel import *
from shop.scraping.scrapping_tottus import *

import json

def redireccionar(request):
    # Reemplaza 'ruta_destino' con el nombre de la ruta a la que deseas redirigir
    return redirect('moderator/addProduct')

@csrf_exempt
def get_product(request):
    if request.method == 'POST':
        try:
            campo1 = request.POST['campo1']
            campo2 = request.POST['campo2']
            campo3 = request.POST['campo3']
            campo4 = request.POST['campo4']
            objeto = ScrappingUtil()
            return objeto.scrappingData(request,campo1, campo2, campo3, campo4)
            # Aquí puedes llamar al método que desees ejecutar con los valores de los campos
           
        except Exception as e:
            error_message = "Ocurrió un error: " + str(e)
            error_data = {"error": error_message}
            return HttpResponseBadRequest(json.dumps(error_data), content_type="application/json")
        
@csrf_exempt
def get_product_price(request):
    if request.method == 'POST':
        try:
            campo1 = request.POST['campo1']
            campo2 = request.POST['campo2']
            campo3 = request.POST['campo3']
            campo4 = request.POST['campo4']
            objeto = ScrappingUtil()
            return objeto.scrappingData(request,campo1, campo2, campo3, campo4)
            # Aquí puedes llamar al método que desees ejecutar con los valores de los campos
           
        except Exception as e:
            error_message = "Ocurrió un error: " + str(e)
            error_data = {"error": error_message}
            return HttpResponseBadRequest(json.dumps(error_data), content_type="application/json")        

@csrf_exempt
def prueba_unimarc(request):
    result = scrappingUnimarc("https://www.unimarc.cl/product/queso-parmesano-rallado-dos-alamos-80-g")
    print("Marca del producto:", result[0])
    print("Nombre del producto:", result[1])
    print("Precio del producto:", result[2])
    print("URL de la imagen:", result[3])
    print("---------------------------------------")
  
    return JsonResponse({})

@csrf_exempt
def prueba_jumbo(request):
    result = scrappingJumbo("https://www.jumbo.cl/queso-parmesano-soprole-80-g-2/p")
    print("Marca del producto:", result[0])
    print("Nombre del producto:", result[1])
    print("Precio del producto:", result[2])
    print("URL de la imagen:", result[3])
    print("---------------------------------------")
  
    return JsonResponse({})

@csrf_exempt
def prueba_santa_isabel(request):
    result = scrappingSantaIsabel("https://www.santaisabel.cl/queso-parmesano-soprole-80-g-2/p")
    print("Marca del producto:", result[0])
    print("Nombre del producto:", result[1])
    print("Precio del producto:", result[2])
    print("URL de la imagen:", result[3])
    print("---------------------------------------")
  
    return JsonResponse({})



@csrf_exempt
def prueba_lider(request):
    result = scrappingLider("https://www.lider.cl/supermercado/product/sku/277418/soprole-queso-rallado-parmesano-80-g")
    print("Marca del producto:", result[0])
    print("Nombre del producto:", result[1])
    print("Precio del producto:", result[2])
    print("URL de la imagen:", result[3])
    print("---------------------------------------")
  
    return JsonResponse({})