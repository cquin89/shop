from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from shop.utils.ScrapingUtil import ScrappingUtil
from shop.models import Category
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponseBadRequest

import json
from shop.models import *
from shop.api.serializers import *

def redireccionar(request):
    # Reemplaza 'ruta_destino' con el nombre de la ruta a la que deseas redirigir
    return redirect('moderator/addProduct')

@csrf_exempt
def mi_formulario(request):
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


