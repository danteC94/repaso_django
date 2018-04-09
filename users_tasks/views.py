from django.views.generic.base import TemplateView
from .forms import TaskForm, EventbriteForm, GoogleMapsModelForm
from .models import Task, Event
from django.views.generic.edit import (
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from eventbrite import Eventbrite


@method_decorator(login_required, name='dispatch')
class Index(TemplateView, LoginRequiredMixin):
    template_name = 'index.html'
    # 'django.contrib.auth',
    # 'social_django',


class TaskList(TemplateView):
    template_name = 'list_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('list_task')

    def get_context_data(self, **kwargs):
        context = super(
            TaskList,
            self
        ).get_context_data(**kwargs)
        context['task_list'] = Task.objects.all()
        return context


class TaskCreateView(CreateView):
    template_name = 'create_task.html'
    model = Task
    fields = ['name', 'description', 'finished', 'priority', 'user']
    success_url = reverse_lazy('list_task')


class TaskUpdateView(UpdateView):
    template_name = 'update_task.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('list_task')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('list_task')


''' Otra forma de crear la vista'''

# class TaskCreateView(CreateView):
#     model = Task
#     fields = ['name', 'description', 'finished', 'priority', 'user']
#     template_name = "new_task.html"
#     success_url = reverse_lazy('list_task')

#     def get_context_data(self, **kwargs):
#         context = super(
#             TaskCreateView,
#             self
#         ).get_context_data(**kwargs)
#         form = TaskForm()
#         context['form'] = form
#         return context


#     def post(self, request, *args, **kwargs):
#         #form = self.get_form()
#         new_form = TaskForm(request.POST)
#         if new_form.is_valid():
#             #import ipdb; ipdb.set_trace()
#             return self.form_valid(new_form)
#         else:
#             return self.form_invalid(new_form)

#     def form_valid(self, new_form):
#         #import ipdb; ipdb.set_trace()
#         new_form.save()
#         return super(
#             TaskCreateView,
#             self,
#         ).form_valid(new_form)
'''fin creacion tarea'''


class EventbriteSocialView(FormView):
    form_class = EventbriteForm
    template_name = 'events.html'
    success_url = reverse_lazy('index')

    def get_api_events(self, social_auth):
        access_token = social_auth.access_token
        eventbrite = Eventbrite(access_token)
        return eventbrite.get('/users/me/events/')['events']

    def get_context_data(self, **kwargs):
        context = super(
            EventbriteSocialView,
            self
        ).get_context_data(**kwargs)
        social_auth = self.request.user.social_auth.get(
            provider='eventbrite'
        )
        if social_auth:
            events = self.get_api_events(social_auth)
        # import ipdb; ipdb.set_trace()
        event_list = []
        for event in events:
            new_event = Event()
            new_event.title = event['name']['text']
            if event['logo'] is not None:
                new_event.image = event['logo']['url']
            event_list.append(new_event)
        context['event_list'] = event_list
        return context


# class EventbriteAccessDenied(TemplateView):
#     template_name = 'access_denied'


class GoogleMapsView(FormView):
    template_name = 'google_maps.html'
    form_class = GoogleMapsModelForm
    success_url = reverse_lazy('index')







