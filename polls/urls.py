from django.urls import path
from .views import UserRegisterView, PollListCreateView, PollDetailView

urlpatterns = [

    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('polls/', PollListCreateView.as_view(), name='poll-list-create'),
    path('polls/<int:pk>/', PollDetailView.as_view(), name='poll-detail'),
]