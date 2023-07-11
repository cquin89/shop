
from django.contrib import messages
from shop.utils.utils import *
from shop.utils.ModelsUtils import *
from shop.scraping.scrapping_jumbo import scrappingJumbo
from shop.scraping.scrapping_santaisabel import scrappingSantaIsabel
from shop.scraping.scrapping_unimarc import scrappingUnimarc
from shop.scraping.scrapping_lider import scrappingLider
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.http import JsonResponse

class ScrappingUtil:
 
    def verificateMarket(self,url):
        if(contiene_palabra(url,"jumbo.cl")):
            return 1
        elif(contiene_palabra(url,"santaisabel.cl")):
            return 1
        elif(contiene_palabra(url,"unimarc.cl")):
            return 1
        elif(contiene_palabra(url,"lider.cl")):
            return  1
        else:
            return 0
        
    def scrappingData(self,request,campo1, campo2, campo3, campo4):
        validation = 0
        if (validateUrl(campo1) is False):
            raise Exception('Hubo un error al procesar el campo 1.') 
        elif (validateUrl(campo2) is False):
            raise Exception('Hubo un error al procesar el campo 2.' ) 
        elif (validateUrl(campo3) is False):
            raise Exception('Hubo un error al procesar el campo 3.' ) 
        elif (validateUrl(campo4) is False):
            raise Exception('Hubo un error al procesar el campo 4.' )     
        else:
            validation +=self.verificateMarket(campo1)
            validation += self.verificateMarket(campo2)
            validation += self.verificateMarket(campo3)
            validation += self.verificateMarket(campo4)
            print(validation)
            if(validation!=4):
                raise Exception('Falto un supermercado')
            else:
                return self.getScrapingData(request,campo1,campo2,campo3,campo4)
   
    def getScrapingData(self,request,campo1, campo2, campo3, campo4):
        resultados = []
        try:
            resultado1 = scrappingJumbo(campo1)
            resultados.append(resultado1)
        except Exception as e:
            raise Exception('Error obteniendo data campo 1 jumbo')
        try:
            resultado3 = scrappingSantaIsabel(campo3)
            resultados.append(resultado3)
        except Exception as e:
            raise Exception('Error obteniendo data campo 3 santa isabel')
        try:
            resultado4 = scrappingUnimarc(campo4)
            resultados.append(resultado4)
        except Exception as e:
            raise Exception('Error obteniendo data campo 4 unimarc')
        try:
            resultado2 = scrappingLider(campo2)
            resultados.append(resultado2)
        except Exception as e:
            raise Exception('Error obteniendo data campo 2 lider')
        # Validar que los resultados contengan los cuatro valores
        if len(resultados) == 4:
            print("¡Se obtuvieron los cuatro resultados correctamente!")
             # Imprimir los resultados
            for resultado in resultados:
                print("Marca del producto:", resultado[0])
                print("Nombre del producto:", resultado[1])
                print("Precio del producto:", resultado[2])
                print("URL de la imagen:", resultado[3])
                print("---------------------------------------")

      
            productUtils = ProductUtils()
            return productUtils.createProduct(request,resultados)
        else:
            raise Exception('Falto al obtener productos.')

       



    def scrapingValues(self,url):
        if(contiene_palabra(url,"jumbo.cl")):
            return scrappingJumbo(url)
        elif(contiene_palabra(url,"santaisabel.cl")):
            return scrappingSantaIsabel(url)
        elif(contiene_palabra(url,"unimarc.cl")):
            return scrappingUnimarc(url)
        elif(contiene_palabra(url,"lider.cl")):
            return  scrappingLider(url)
    # elif(contiene_palabra(url,"falabella.com")):
    #      return scrappingTottus(url)
        else:
            return None

