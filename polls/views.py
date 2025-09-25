from django.db.models import Count
from django.shortcuts import render
from django.utils import timezone
from rest_framework.response import Response

from .models import Poll, Vote
from .serializers import UserSerializer, PollSerializer, VoteSerializer, PollResultSerializer
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated


# User Registration View
class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class PollListCreateView(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class PollDetailView(generics.RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [AllowAny]


class VoteCreateView(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]
    queryset = Vote.objects.none()


    def create(self, request, *args, **kwargs):
        poll_id = self.kwargs.get('pk')
        try:
            poll = Poll.objects.get(pk=poll_id)
        except Poll.DoesNotExist:
            return Response({'error': 'Poll not found.'}, status=status.HTTP_404_NOT_FOUND)

        if poll.expiry_date and poll.expiry_date < timezone.now():
            return Response({'error': 'This poll has expired.'}, status=status.HTTP_400_BAD_REQUEST)

        if Vote.objects.filter(poll=poll, user=request.user).exists():
            return Response({'error': 'You have already voted on this poll.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        choice = serializer.validated_data['choice']

        if choice.poll != poll:
            return Response({'error': 'This choice is not valid for this poll.'}, status=status.HTTP_400_BAD_REQUEST)


        Vote.objects.create(user=request.user, poll=poll, choice=choice)

        return Response({'message': 'Your vote has been recorded!'}, status=status.HTTP_201_CREATED)


# Poll Results View
class PollResultsView(generics.RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollResultSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):

        queryset = super().get_queryset().prefetch_related(
            'choices'
        ).annotate(

        )
        return queryset


    def retrieve(self, request, *args, **kwargs):
        poll = self.get_object()
        choices_with_votes = poll.choices.annotate(vote_count=Count('vote'))

        total_votes = sum(choice.vote_count for choice in choices_with_votes)

        choices_data = []
        for choice in choices_with_votes:
            # Calculate the percentage.
            percentage = (choice.vote_count / total_votes) * 100 if total_votes > 0 else 0
            choices_data.append({
                'id': choice.id,
                'choice_text': choice.choice_text,
                'vote_count': choice.vote_count,
                'percentage': round(percentage, 1)
            })

        data = {
            'id': poll.id,
            'questions': poll.questions,
            'total_votes': total_votes,
            'choices': choices_data
        }
        return Response(data)