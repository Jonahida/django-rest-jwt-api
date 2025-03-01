from django.urls import path
from .views import RegisterUserView, LoginUserView, SecureApiView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('secure/', SecureApiView.as_view(), name='secure-api'),
]

