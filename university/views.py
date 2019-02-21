# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from mylib.mygenerics import MyListCreateAPIView, MyDjangoFilterBackend
from university.course.serializers import CourseSerializer
from university.models import University, Course
from university.serializers import UniversitySerializer


class ListCreateUniversitysAPIView(generics.ListCreateAPIView):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()
    filter_backends = (MyDjangoFilterBackend,)

class RetrieveUpdateDestroyUniversityAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()
    

class ListCreateUniversityCoursesAPIView(MyListCreateAPIView):
    foreign_key_field="university"
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_backends = (MyDjangoFilterBackend,)