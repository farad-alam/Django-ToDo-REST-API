from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import UserDetailedUpdateDeleteView, UserCreateListView, UserRegistrationView, LogoutView

urlpatterns = [
    path('user-create/', UserCreateListView.as_view(), name='user-create'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    #  path('users/', UserListView.as_view(), name='user-list'),
     path('users/<int:id>/', UserDetailedUpdateDeleteView.as_view(), name='user-detailed-update'),

    path('logout/', LogoutView.as_view(), name='logout'),
    path('request-password-reset/', views.request_password_reset, name='request-password-reset'),
    path('reset-password/', views.reset_password, name='reset-password'),
    path('token-verify/', views.verify_password_restet_token, name='token-verify'),

    path('token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),


    #View URL
    path('request-password-reset-view/', views.request_password_reset_view, name='request-password-reset-view'),
    path('reset-account-password/', views.reset_password_view, name='reset-password-view'),
    path('login-view/', views.login_view, name='login-view')
    
]

