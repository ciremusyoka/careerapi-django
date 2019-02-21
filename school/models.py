# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from mylib.my_common import MyAbstractModel, COUNTIES


class School(MyAbstractModel):
    name=models.CharField(max_length=45,unique=True)
    county=models.CharField(choices=COUNTIES,max_length=30)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.name


class Subject(MyAbstractModel):
    groups=(('1','Group 1'),('2','Group 2'))
    name=models.CharField(max_length=44,unique=True)
    group=models.CharField(choices=groups,max_length=2,default="1")

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.name


