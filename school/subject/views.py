# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from rest_framework import generics

from mylib.mygenerics import MyDjangoFilterBackend
from school.models import Subject
from school.subject.serializers import SubjectSerializer


class ListCreateSubjectsAPIView(generics.ListCreateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    filter_backends = (MyDjangoFilterBackend,)


class RetrieveUpdateDestroySubjectAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
