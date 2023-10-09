from rest_framework import serializers

from network.models import NetworkNode


class NetworkNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = '__all__'