from __future__ import unicode_literals
from django.db import models
class Tag(models.Model):
    tag_name = models.CharField(max_length=200)
    def __str__(self):
        return self.tag_name
# Create your models here.
