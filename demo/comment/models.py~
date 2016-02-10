from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from question.models import Question
class Comment(models.Model):  
     user = models.ForeignKey(User)
     question_id = models.ForeignKey(Question)  
     comment = models.CharField(max_length = 200)

