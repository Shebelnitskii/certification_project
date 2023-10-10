from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'phone', 'is_active', 'is_staff')

    def create(self, validated_data):
        """ Хеширование пароля при создании нового пользователя в БД """
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """ Хеширование пароля при изменении пароля пользователя """
        # Проверяем, есть ли поле "password" в validated_data
        if 'password' in validated_data:
            # Если есть, хешируем новый пароль
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)