from rest_framework.routers import DefaultRouter
from shop.api.views import BrandApiViewSet
from shop.api.views import ProductApiViewSet
route_posts = DefaultRouter()

route_posts.register(prefix='brand',basename='brand',viewset=BrandApiViewSet)
route_posts.register(prefix='product',basename='product',viewset=ProductApiViewSet)