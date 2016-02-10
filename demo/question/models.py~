from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
class Question(models.Model):
   user = models.ForeignKey(User)
   question_title = models.CharField(max_length = 200)
   question_body = models.CharField(max_length = 1000)
   tag = models.ManyToManyField('tag.Tag')
   point = models.IntegerField(default = 0)
   answer = models.ManyToManyField('answer.Answer', blank = True)
   question_comment = models.CharField('comment.Comment',max_length = 200,blank = True)
   def __unicode__(self):
        return self.question_title
# Create your models here.
