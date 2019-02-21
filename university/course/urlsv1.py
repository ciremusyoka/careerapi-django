from django.conf.urls import url

from university.course.views import ListCreateCoursesAPIView, RetrieveUpdateDestroyCourseAPIView, \
    ListCreateCoursesCutoffsAPIView

urlpatterns=[
    url(r'^$',ListCreateCoursesAPIView.as_view(),name="list_create_courses"),
    url(r'^(?P<pk>[0-9]+)/?$',RetrieveUpdateDestroyCourseAPIView.as_view(),name="retrieve_update_destroy_course"),
    url(r'^(?P<pk>[0-9]+)/cutoffs/?$',ListCreateCoursesCutoffsAPIView.as_view(),name="list_create_courses_cutoffs"),
]