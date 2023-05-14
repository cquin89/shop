from rest_framework.viewsets import ModelViewSet
from shop.models import Brand
from shop.models import Product
from shop.api.serializers import BrandSerilizer
from shop.api.serializers import ProductSerilizer

class BrandApiViewSet(ModelViewSet):
    serializer_class = BrandSerilizer
    queryset = Brand.objects.all()


class ProductApiViewSet(ModelViewSet):
    serializer_class = ProductSerilizer
    queryset = Product.objects.all()