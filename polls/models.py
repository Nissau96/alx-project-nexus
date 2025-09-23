from django.db import models
from django.contrib.auth.models import User

# Poll Model
class Poll(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.questions

# Choice Model.
class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)


    def __str__(self):
        return self.choice_text

# Vote Model
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)


    class Meta:
        unique_together = ('user', 'poll')