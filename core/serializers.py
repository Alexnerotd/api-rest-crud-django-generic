from rest_framework import serializers
from django.contrib import messages
from .models import MyUser

class MyUserSerializerGET(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'name', 'last_name']

    
class MyUserSerializerPOST(serializers.ModelSerializer):

    class Meta:
        model = MyUser  # Agrega esta línea para especificar el modelo
        fields = ['username', 'email', 'password', 'name', 'last_name']

    
    def create(self, validated_data):
        user = MyUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

