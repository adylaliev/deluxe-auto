from django.urls import path, include
from rest_framework.routers import SimpleRouter

from products.views import ProductViewSet, CommentViewSet

router = SimpleRouter()
router.register('products', ProductViewSet, 'products')
router.register('comments', CommentViewSet, 'comments')

urlpatterns = [
    path('', include(router.urls))
]

