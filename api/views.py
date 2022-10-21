from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class AuthUserRegistrationView(APIView):
	def post(self, request, *args, **kwargs):
		serializer =UserSerializer(data=request.data)
		for user in User.objects.all():
			if not user:
				break
			else:
				try:
					Token.objects.get(user_id=user.id)
				except Token.DoesNotExist:
					Token.objects.create(user=user)
		if serializer.is_valid():
			user =serializer.save()
			token =Token.objects.create(user=user)
			return Response(
				{
					"user": {
						"id":serializer.data["id"],
						"username":serializer.data["username"],
						"password":serializer.data["password"]
					},
					"status": {
						"message": "User created",
						"code": f"{status.HTTP_200_OK} OK",
					},
					"token": token.key,
				}
			)
		return Response(
			{
				"error": serializer.errors,
				"status": f"{status.HTTP_203_NON_AUTHORITATIVE_INFORMATION}\
				NON AUTHORITATIVE INFORMATION",
			}
		)		


class menuSerializerView(ListCreateAPIView):
	permission_classes =(permissions.IsAuthenticated,)
	queryset =Menu.objects.all()
	serializer_class =menuSerializers

class menuIDSerializerView(RetrieveUpdateDestroyAPIView):
	permission_classes =(permissions.IsAuthenticated,)
	queryset =Menu.objects.all()
	serializer_class =menuSerializers



# Create your views here.
