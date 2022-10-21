from rest_framework import serializers
from .models import Menu, User
from rest_framework.generics import ListAPIView

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

	def create(self, validated_data):
		auth_user = User.objects.create_user(**validated_data)
		return auth_user

class menuSerializers(serializers.ModelSerializer):
	class Meta:
		model =Menu
		fields ='__all__'