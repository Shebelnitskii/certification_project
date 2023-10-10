from rest_framework import serializers
from network.models import NetworkNode, Contact, Product


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = NetworkNode
        fields = '__all__'

    def update(self, instance, validated_data):
        if 'debt' in validated_data:
            raise serializers.ValidationError("Нельзя изменять задолженность.")
        return super().update(instance, validated_data)
