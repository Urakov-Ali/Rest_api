from django.urls import path
from .views import *

urlpatterns =[
	path('', menuSerializerView.as_view()),
	path('<int:pk>/', menuIDSerializerView.as_view()),
	path('register/',AuthUserRegistrationView.as_view())
	]