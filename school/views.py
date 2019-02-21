# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from school.models import School
from school.serializers import SchoolSerializer


class ListCreateSchoolsAPIView(generics.ListCreateAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()


class RetrieveUpdateDestroySchoolAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()