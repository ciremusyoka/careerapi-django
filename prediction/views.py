# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from mylib.mygenerics import MyDjangoFilterBackend
from prediction.models import Prediction
from prediction.serializers import PredictionSerializer


class ListCreatePredictions(generics.ListCreateAPIView):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer
    filter_backends = (MyDjangoFilterBackend,)


class RetrieveUpdateDestroyPredictions(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer