from rest_framework.serializers import ModelSerializer
from shop.models import *

class BrandSerilizer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id','name']

class CategorySerilizer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']        

class StoreSerilizer(ModelSerializer):
    class Meta:
        model = Store
        fields = ['id','name','logoUrl']                

class ProductSerilizer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','pictureUrl','brand','category']