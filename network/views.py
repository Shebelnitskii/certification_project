from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from network.models import NetworkNode, Product, Contact
from network.permissions import IsActiveOwner
from network.serializers import NetworkNodeSerializer, ProductSerializer, ContactSerializer


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

class ProductListAPI(generics.ListAPIView):
    """ Просмотр списка продуктов"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveOwner]

class ProductCreateAPI(generics.CreateAPIView):
    """ Создание продукта """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveOwner]

class ProductDetailAPI(generics.RetrieveAPIView):
    """ Просмотр деталей конкретного продукта """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveOwner]

class ProductUpdateAPI(generics.UpdateAPIView):
    """ Обновление данных о продукте """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveOwner]

class ProductDeleteAPI(generics.DestroyAPIView):
    """ Удаление продукта """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveOwner]


class ContactListAPI(generics.ListAPIView):
    """ Просмотр списка контактов"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsActiveOwner]


class ContactCreateAPI(generics.CreateAPIView):
    """ Создание контакта """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsActiveOwner]


class ContactDetailAPI(generics.RetrieveAPIView):
    """ Просмотр деталей конкретного контакта """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsActiveOwner]


class ContactUpdateAPI(generics.UpdateAPIView):
    """ Обновление данных о контакте """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsActiveOwner]


class ContactDeleteAPI(generics.DestroyAPIView):
    """ Удаление контакта """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsActiveOwner]