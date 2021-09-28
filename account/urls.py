from django.urls import path

from .views import RegistrationView, ActivationView, LoginView, LogOutView, ForgotPasswordView, \
    ForgotPasswordCompleteView, ChangePasswordView

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='регистрация-аккаунта'),
    path('activate/', ActivationView.as_view(), name='аккаунт-активирован'),
    path('login/', LoginView.as_view(), name='авторизация'),
    path('logout/', LogOutView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('forgot_password/complete/', ForgotPasswordCompleteView.as_view()),
    path('change_password', ChangePasswordView.as_view())
]