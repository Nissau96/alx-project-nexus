from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

# User Registration View
class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]