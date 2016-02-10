from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):  
     user = models.ForeignKey(User)
    
     gender = models.CharField(max_length=140)  
     email = models.EmailField(max_length=70,blank=True,null= True)
     def __unicode__(self):
        return self.user.username

