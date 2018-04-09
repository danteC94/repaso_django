from django.conf.urls import url
from .views import (
    Index,
    TaskList,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    EventbriteSocialView,
    # EventbriteAccessDenied,
    GoogleMapsView,
)


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
    url(r'eventbrite_index/$',
        EventbriteSocialView.as_view(),
        name='eventbrite',
        ),
    # url(r'complete/eventbrite/(?P<string>[a-z]+)',
    #     EventbriteAccessDenied.as_view(template_name='access_denied.html'),
    #     name='access_denied',
    #     )
    url(r'google_maps_test/$',
        GoogleMapsView.as_view(),
        name='google_maps',
        ),
]
