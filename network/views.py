from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from network.models import NetworkNode
from network.permissions import IsActiveOwner
from network.serializers import NetworkNodeSerializer


# Create your views here.

class NetworkNodeListAPI(generics.ListAPIView):
    """ Просмотр списка поставщиков"""
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    filter_backends = [DjangoFilterBackend] # Возможность вывода информации по конкретной стране
    permission_classes = [IsActiveOwner, IsAuthenticated]

    def get_queryset(self):
        """ Возможность фильтрации по стране в админке django """
        queryset = super().get_queryset()
        country = self.request.query_params.get('country')
        if country:
            # Фильтруем объекты по стране
            queryset = queryset.filter(contact__country=country)
        return queryset


class NetworkNodeCreateAPI(generics.CreateAPIView):
    """ Создание поставщика """
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveOwner]


class NetworkNodeDetailAPI(generics.RetrieveAPIView):
    """ Просмотр деталей конкретного поставщика """
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveOwner, IsAuthenticated]


class NetworkNodeUpdateAPI(generics.UpdateAPIView):
    """ Обновление данных о поставщике """
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveOwner]


class NetworkNodeDeleteAPI(generics.DestroyAPIView):
    """ Удаление поставщика """
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveOwner]
