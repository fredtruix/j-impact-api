from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .apis import UserRegisterView,ProfileDetailsView,MyTokenObtainPairView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # profile
    path('profile/', ProfileDetailsView.as_view(), name="profiledetails")
    
]
