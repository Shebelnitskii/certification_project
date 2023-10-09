from rest_framework import serializers

from network.models import NetworkNode


class NetworkNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = '__all__'

    def update(self, instance, validated_data):
        if 'debt' in validated_data:
            raise serializers.ValidationError("Нельзя изменять задолженность.")
        return super().update(instance, validated_data)