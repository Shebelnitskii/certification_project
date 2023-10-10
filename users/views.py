from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import User
from .permissions import IsOwnerOrModerator
from .serializers import UserSerializer


# Create your views here.
class UserListAPI(generics.ListCreateAPIView):
    """ Вывод информации о пользователях, может каждый """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailAPI(generics.RetrieveAPIView):
    """ Детали пользователя, может каждый"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserCreateAPI(generics.CreateAPIView):
    """ Создать пользователя, может каждый """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserUpdateAPI(generics.UpdateAPIView):
    """ Изменить пользователя, может либо сам пользователь либо модератор """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrModerator]


class UserDeleteAPI(generics.DestroyAPIView):
    """ Удалить пользователя, может либо сам пользователь либо модератор """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrModerator]
