from django.conf.urls import url

from university.views import ListCreateUniversitysAPIView, RetrieveUpdateDestroyUniversityAPIView, \
    ListCreateUniversityCoursesAPIView

urlpatterns=[
    url(r'^$',ListCreateUniversitysAPIView.as_view(),name="list_create_universitys"),
    url(r'^(?P<pk>[0-9]+)/?$',RetrieveUpdateDestroyUniversityAPIView.as_view(),name="retrieve_update_destroy_university"),
    url(r'^(?P<pk>[0-9]+)/courses/?$',ListCreateUniversityCoursesAPIView.as_view(),name="list_create_university_courses"),
]