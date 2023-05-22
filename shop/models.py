from django.db import models

class Store(models.Model):
        name = models.CharField(max_length=200)
        logoUrl = models.CharField(max_length=200, null=True) 
        color = models.CharField(max_length=30, null=True) 
        def __str__(self):
                return f'{self.name}'
        
class Brand(models.Model):
        name = models.CharField(max_length=200)

        def __str__(self):
                return f'{self.name}'

class Category(models.Model):
        name = models.CharField(max_length=200)
        imageUrl = models.CharField(max_length=200, null=True)

        def __str__(self):
                return f'{self.name}'

class Product(models.Model):
        name = models.CharField(max_length=200)
        pictureUrl = models.CharField(max_length=200, null=True) 
        brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
        category = models.ForeignKey(Category, on_delete=models.CASCADE)

        def __str__(self):
                return f'{self.id} - {self.name}'
        

class ProductDetailt(models.Model):
        nameStoreProduct = models.CharField(max_length=200)
        price = models.FloatField(default=0)
        url = models.CharField(max_length=200) 
        store = models.ForeignKey(Store, on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)