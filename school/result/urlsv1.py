from django.conf.urls import url

from school.result.views import ListCreateResultsAPIView, RetrieveUpdateDestroyResultAPIView, \
    ListCreateResultSubjectResultsAPIView

urlpatterns=[
    url(r'^$',ListCreateResultsAPIView.as_view(),name="list_create_results"),
    url(r'^(?P<pk>[0-9]+)/?$',RetrieveUpdateDestroyResultAPIView.as_view(),name="retrieve_update_destroy_result"),
    url(r'^(?P<pk>[0-9]+)/subjects/?$',ListCreateResultSubjectResultsAPIView.as_view(),name="list_create_result_subject_results"),
]