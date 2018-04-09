from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from .views import Index, TaskList, TaskCreateView, TaskUpdateView, TaskDeleteView


urlpatterns = [

    url(r'^$',
        Index.as_view(template_name='index.html'),
        name='index',
        ),
    url(r'^list_task$',
        TaskList.as_view(),
        name='list_task',
        ),
    url(r'^create_task$',
        TaskCreateView.as_view(),
        name='new_task',
        ),
    url(r'task_update/(?P<pk>[0-9]+)/$',
        TaskUpdateView.as_view(),
        name='task_update'
        ),
    url(r'^(?P<pk>[0-9]+)/task_delete/$',
        TaskDeleteView.as_view(),
        name='task_delete'
        ),
]