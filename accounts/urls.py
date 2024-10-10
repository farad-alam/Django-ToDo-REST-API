from django.urls import path
from . import views

from django.urls import path
from .views import UserDetailedUpdateDeleteView, UserCreateListView

urlpatterns = [
    path('user-create/', UserCreateListView.as_view(), name='user-create'),
    path('registration/', views.registration_view, name='registration'),
    #  path('users/', UserListView.as_view(), name='user-list'),
     path('users/<int:id>/', UserDetailedUpdateDeleteView.as_view(), name='user-detailed-update'),

    path('request-password-reset/', views.request_password_reset, name='request-password-reset'),
    path('reset-password/', views.reset_password, name='reset-password'),
    path('token-verify/', views.verify_password_restet_token, name='token-verify')
]

