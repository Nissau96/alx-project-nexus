from django.urls import path
from .views import UserRegisterView, PollListCreateView, PollDetailView, VoteCreateView, PollResultsView

urlpatterns = [

    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('polls/', PollListCreateView.as_view(), name='poll-list-create'),
    path('polls/<int:pk>/', PollDetailView.as_view(), name='poll-detail'),
    path('polls/<int:pk>/vote/', VoteCreateView.as_view(), name='poll-vote'),
    path('polls/<int:pk>/results/', PollResultsView.as_view(), name='poll-results'),
]