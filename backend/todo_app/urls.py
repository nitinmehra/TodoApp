from django.urls import path,re_path
from todo_app.viewsets import TodoViewSet
from django.conf.urls import url

urlpatterns = [
    url('^getall/$', TodoViewSet.as_view({'get':'list'}), name='todo_list' ),
    url('^create/$', TodoViewSet.as_view({'post':'create'}), name='todo_create' ),
    url('^get/(?P<id>[0-9]+)/$', TodoViewSet.as_view({'get':'retrieve'}), name='todo_detail' ),
    url('^put/(?P<id>[0-9]+)/$', TodoViewSet.as_view({'put':'update'}), name='todo_update' ),
    url('^delete/(?P<id>[0-9]+)/$', TodoViewSet.as_view({'delete':'destroy'}), name='todo_delete' ),
]
