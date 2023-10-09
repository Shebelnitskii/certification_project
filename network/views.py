from django.shortcuts import render
from rest_framework import generics
from network.models import NetworkNode
from network.serializers import NetworkNodeSerializer


# Create your views here.


class NetworkNodeListAPI(generics.ListAPIView):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer


class NetworkNodeCreateAPI(generics.CreateAPIView):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer


class NetworkNodeDetailAPI(generics.RetrieveAPIView):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer


class NetworkNodeUpdateAPI(generics.UpdateAPIView):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer


class NetworkNodeDeleteAPI(generics.DestroyAPIView):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
