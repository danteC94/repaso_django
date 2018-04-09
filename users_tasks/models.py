from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone
from django_google_maps import fields as map_fields


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


class Event(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=5000)


class GoogleMapsModel(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
