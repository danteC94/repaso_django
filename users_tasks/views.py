from django.views.generic.base import TemplateView
from .forms import TaskForm
from .models import Task
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


@method_decorator(login_required, name='dispatch')
class Index(TemplateView, LoginRequiredMixin):
    template_name = 'index.html'


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














