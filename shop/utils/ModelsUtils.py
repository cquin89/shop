from shop.models import *
from django.contrib import messages

class ProductUtils:

    def createProduct(self,request,resultados):
        categoryId = request.POST.get('categoria')
        productBrand = self.find_repeited_brand(resultados)
        brand = self.getBrandByName(productBrand)
        if(brand is None):
            brand = Brand()
            brand.name = productBrand
            brand.save
        primerProducto = resultados[0]
        newProduct = Product()
        newProduct.brand = brand
        newProduct.category = self.getCategoryById(categoryId)
        newProduct.name = primerProducto[1]
        newProduct.pictureUrl = primerProducto[3]
        newProduct.save

        for resultado in resultados:
            productDetailt = ProductDetailt()
            productDetailt.product = newProduct
            productDetailt.store = self.getStoreByName(resultado[4])
            productDetailt.price = resultado[2]
            productDetailt.url = resultado[5]
            productDetailt.nameStoreProduct = resultado[1]
            productDetailt.save
        messages.success(request, 'Se obtuvieron todos los productos')  
        
    def getBrandByName(nombre):
        try:
            brand = Brand.objects.get(name=nombre)
            return brand
        except Brand.DoesNotExist:
            return None
        
    def getStoreByName(nombre):
        try:
            store = Store.objects.get(name=nombre)
            return store
        except Store.DoesNotExist:
            return None

    def find_repeited_brand(resultados):
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
    
    def getCategoryById(categoria_id):
        try:
            categoria = Category.objects.get(id=categoria_id)
            return categoria
        except Category.DoesNotExist:
            return None