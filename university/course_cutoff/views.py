# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from mylib.mygenerics import MyDjangoFilterBackend
from university.course_cutoff.serializers import CourseCutoffSerializer
from university.models import CourseCutoff


class ListCreateCourseCutoffsAPIView(generics.ListCreateAPIView):
    serializer_class = CourseCutoffSerializer
    queryset = CourseCutoff.objects.all()
    filter_backends = (MyDjangoFilterBackend,)


class RetrieveUpdateDestroyCourseCutoffAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseCutoffSerializer
    queryset = CourseCutoff.objects.all()