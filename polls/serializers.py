
from django.contrib.auth.models import User
from rest_framework import serializers

from polls.models import Choice, Poll, Vote


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

# Choice Serializer
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text']


# Poll Model Serializer
class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    owner = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Poll
        fields = ['id', 'questions', 'pub_date', 'expiry_date', 'creator', 'choices']


    def create(self, validated_data):

        choices_data = validated_data.pop('choices')
        poll = Poll.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(poll=poll, **choice_data)

        return poll

# Vote Serializer
class VoteSerializer(serializers.ModelSerializer):
    choice = serializers.PrimaryKeyRelatedField(queryset=Choice.objects.all())

    class Meta:
        model = Vote
        fields = ['choice']


# Result Serializer
class ChoiceResultSerializer(serializers.ModelSerializer):
    vote_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Choice
        fields = ('id', 'choice_text', 'vote_count')



# Poll Result Serializer
class PollResultSerializer(serializers.ModelSerializer):
    # I'm using the ChoiceResultSerializer I just made to handle the list of choices.
    choices = ChoiceResultSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ('id', 'questions', 'choices')