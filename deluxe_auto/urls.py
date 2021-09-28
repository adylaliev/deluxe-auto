"""deluxe_auto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from account.views import RegistrationView, ActivationView, LoginView, LogOutView, ForgotPasswordView, \
    ForgotPasswordCompleteView, ChangePasswordView
from orders.views import PurchasesView
from products.views import ProductViewSet, CommentViewSet, LikesView

router = DefaultRouter()
router.register('product', ProductViewSet, 'products')
router.register('comments', CommentViewSet, 'comments')
router.register('likes', LikesView, 'likes')
router.register('rating', PurchasesView, 'rating')

schema_view = get_schema_view(
    openapi.Info(
          title="Snippets API",
          default_version='v1',
          description="Test description",
          terms_of_service="https://www.google.com/policies/terms/",
          contact=openapi.Contact(email="contact@snippets.local"),
          license=openapi.License(name="BSD License"),
       ),
    public=True,
)

urlpatterns = [
    path('api/v1/docs/', schema_view.with_ui()),
    path('admin/', admin.site.urls),
    path('registration/', RegistrationView.as_view(), name='регистрация-аккаунта'),
    path('activate/', ActivationView.as_view(), name='аккаунт-активирован'),
    path('login/', LoginView.as_view(), name='авторизация'),
    path('logout/', LogOutView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('forgot_password/complete/', ForgotPasswordCompleteView.as_view()),
    path('change_password', ChangePasswordView.as_view()),
    path('', include(router.urls))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)