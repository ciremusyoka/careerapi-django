from django.conf.urls import url

from school.subject_result.views import ListCreateSubjectResultsAPIView, RetrieveUpdateDestroySubjectResultAPIView

urlpatterns=[
    url(r'^$',ListCreateSubjectResultsAPIView.as_view(),name="list_create_subject_results"),
    url(r'^(?P<pk>[0-9]+)/?$',RetrieveUpdateDestroySubjectResultAPIView.as_view(),name="retrieve_update_destroy_subject_result"),
]