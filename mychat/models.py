from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Chat(models.Model):
    user = models.ForeignKey(User)
    message = models.CharField(max_length=300)

    def __unicode__(self):
        return self.message
