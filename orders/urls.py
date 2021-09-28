from django.urls import include, path
from rest_framework.routers import SimpleRouter

from orders.views import AddStarRatingView, LikesView

router = SimpleRouter()
router.register('rating', AddStarRatingView, 'rating')
router.register('like', LikesView, 'likes')

urlpatterns = [
    path('', include(router.urls))
]

