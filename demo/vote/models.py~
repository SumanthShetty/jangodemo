from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
class Vote(models.Model):
    user = models.ForeignKey(User)
    question_id = models.ForeignKey('question.Question', blank = True, null = True)
    answer_id = models.ForeignKey('answer.Answer', blank = True, null = True)
    up_vote = models.IntegerField(default = 200)
    down_vote = models.IntegerField(default = 200)
    is_question = models.BooleanField(default = False)
    is_answer = models.BooleanField(default = False)
    def __unicode__(self):
        return self.user.username
# Create your models here.
