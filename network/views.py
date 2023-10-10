from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from network.models import NetworkNode
from network.permissions import IsActiveOwner
from network.serializers import NetworkNodeSerializer


# Create your views here.

class NetworkNodeListAPI(generics.ListAPIView):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveOwner, IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        country = self.request.query_params.get('country')
        if country:
            # Фильтруем объекты по стране
            queryset = queryset.filter(contact__country=country)
        return queryset


class NetworkNodeCreateAPI(generics.CreateAPIView):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveOwner]


class NetworkNodeDetailAPI(generics.RetrieveAPIView):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveOwner, IsAuthenticated]


class NetworkNodeUpdateAPI(generics.UpdateAPIView):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveOwner]


class NetworkNodeDeleteAPI(generics.DestroyAPIView):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveOwner]
