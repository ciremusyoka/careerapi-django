from django.conf.urls import url

from university.course_cutoff.views import ListCreateCourseCutoffsAPIView, RetrieveUpdateDestroyCourseCutoffAPIView

urlpatterns=[
    url(r'^$',ListCreateCourseCutoffsAPIView.as_view(),name="list_create_course_cutoffs"),
    url(r'^(?P<pk>[0-9]+)/?$',RetrieveUpdateDestroyCourseCutoffAPIView.as_view(),name="retrieve_update_destroy_course_cutoff"),
]