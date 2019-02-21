from django.conf.urls import url

from school.subject.views import ListCreateSubjectsAPIView, RetrieveUpdateDestroySubjectAPIView

urlpatterns=[
    url(r'^$',ListCreateSubjectsAPIView.as_view(),name="list_create_subjects"),
    url(r'^(?P<pk>[0-9]+)/?$',RetrieveUpdateDestroySubjectAPIView.as_view(),name="retrieve_update_destroy_subject"),
]