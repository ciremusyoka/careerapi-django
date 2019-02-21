from django.conf.urls import url

from school.views import ListCreateSchoolsAPIView, RetrieveUpdateDestroySchoolAPIView

urlpatterns=[
    url(r'^$',ListCreateSchoolsAPIView.as_view(),name="list_create_schools"),
    url(r'^(?P<pk>[0-9]+)/?$',RetrieveUpdateDestroySchoolAPIView.as_view(),name="retrieve_update_destroy_school"),
]