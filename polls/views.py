from django.shortcuts import render

from .models import Poll
from .serializers import UserSerializer, PollSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly


# User Registration View
class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class PollListCreateView(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PollDetailView(generics.RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [AllowAny]