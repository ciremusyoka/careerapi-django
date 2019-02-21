from django.conf.urls import url

from prediction.personality.views import ListCreatePersonalitys, RetrieveUpdateDestroyPersonalitys

urlpatterns=[
    url(r'^$', ListCreatePersonalitys.as_view(), name="list_create_personalitys"),
    url(r'^(?P<pk>[0-9]+)/?$', RetrieveUpdateDestroyPersonalitys.as_view(), name="retrieve_update_destroy_personality"),
]