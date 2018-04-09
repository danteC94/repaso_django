from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone


class Priority(models.Model):
    priority = models.CharField(max_length=200)

    def __str__(self):
        return self.priority


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    finished = models.BooleanField()
    priority = models.ForeignKey(Priority)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
