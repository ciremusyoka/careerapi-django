# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from mylib.mygenerics import MyDjangoFilterBackend
from university.models import Profession
from university.profession.serializers import ProfessionSerializer


class ListCreateProfessionsAPIView(generics.ListCreateAPIView):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()
    filter_backends = (MyDjangoFilterBackend,)


class RetrieveUpdateDestroyProfessionAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()