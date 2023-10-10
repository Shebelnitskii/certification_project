from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )
from .views import UserListAPI, UserDetailAPI, UserCreateAPI, UserUpdateAPI, UserDeleteAPI
from django.urls import path

from users.apps import UsersConfig

app_name = UsersConfig.name
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('', UserListAPI.as_view(), name='user_list'),
    path('create/', UserCreateAPI.as_view(), name='user_create'),
    path('detail/<int:pk>/', UserDetailAPI.as_view(), name='user_detail'),
    path('update/<int:pk>/', UserUpdateAPI.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDeleteAPI.as_view(), name='user_delete'),


]
