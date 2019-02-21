from django.conf.urls import url

from university.profession.views import ListCreateProfessionsAPIView, RetrieveUpdateDestroyProfessionAPIView

urlpatterns=[
    url(r'^$',ListCreateProfessionsAPIView.as_view(),name="list_create_professions"),
    url(r'^(?P<pk>[0-9]+)/?$',RetrieveUpdateDestroyProfessionAPIView.as_view(),name="retrieve_update_destroy_profession"),
]