
from django.contrib.auth.models import User
from rest_framework import serializers

from polls.models import Choice, Poll


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
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Poll
        fields = ['id', 'questions', 'pub_date', 'expiry_date', 'creator', 'choices']


    def create(self, validated_data):

        choices_data = validated_data.pop('choices')
        poll = Poll.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(poll=poll, **choice_data)

        return poll