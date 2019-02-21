# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from mylib.mygenerics import MyListCreateAPIView, MyDjangoFilterBackend
from university.course.serializers import CourseSerializer
from university.course_cutoff.serializers import CourseCutoffSerializer
from university.models import Course, CourseCutoff


class ListCreateCoursesAPIView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_backends = (MyDjangoFilterBackend,)


class RetrieveUpdateDestroyCourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()



class ListCreateCoursesCutoffsAPIView(MyListCreateAPIView):
    foreign_key_field="course"
    serializer_class = CourseCutoffSerializer
    queryset = CourseCutoff.objects.all()
    filter_backends = (MyDjangoFilterBackend,)