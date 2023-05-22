from rest_framework.routers import DefaultRouter
from shop.api.views import *
route_posts = DefaultRouter()

route_posts.register(prefix='brand',basename='brand',viewset=BrandApiViewSet)
route_posts.register(prefix='product',basename='product',viewset=ProductApiViewSet)
route_posts.register(prefix='category',basename='category',viewset=CategoryApiViewSet)
route_posts.register(prefix='store',basename='store',viewset=StoreApiViewSet)
