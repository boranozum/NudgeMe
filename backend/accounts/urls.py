from django.urls import path
from rest_framework import routers

from accounts.views.auth import UserVerificationViewSet, RegisterView, LoginView, LoginRefreshView, LogoutView

router = routers.SimpleRouter()

router.register('verification', UserVerificationViewSet, basename='verification')

urlpatterns = router.urls + [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', LoginRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
]