from rest_framework.serializers import ModelSerializer
from shop.models import Brand
from shop.models import Product

class BrandSerilizer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id','name']

class ProductSerilizer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','pictureUrl','brand','category']