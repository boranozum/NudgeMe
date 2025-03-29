from rest_framework import routers
from django.urls import path

from accounts.views.auth import LoginView, LoginRefreshView, LogoutView, RegisterView

router = routers.SimpleRouter()

urlpatterns = router.urls + [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', LoginRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
]