from django.forms import ModelForm
from .models import Task, Event, GoogleMapsModel
from django_google_maps.widgets import GoogleMapsAddressWidget


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'priority', 'user', 'finished', 'id']


class EventbriteForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'image']


class GoogleMapsModelForm(ModelForm):
    class Meta:
        model = GoogleMapsModel
        fields = ['address', 'geolocation']
        widgets = {
            "address": GoogleMapsAddressWidget,
        }
