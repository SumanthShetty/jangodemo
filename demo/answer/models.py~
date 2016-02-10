from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Answer(models.Model):
    user = models.ForeignKey(User)
    answer = models.CharField(max_length = 200)
    is_correct = models.BooleanField(default = False)
    def __str__(self):
        return self.answer
