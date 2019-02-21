# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from mylib.image import scramble
from mylib.my_common import MyAbstractModel
# from prediction.models import Personality
from prediction.personality.models import Personality


class University(MyAbstractModel):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField("uploads", upload_to=scramble, null=True, blank=True)
    aka = models.CharField(max_length=20, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name


class Media(MyAbstractModel):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=1000,null=True,blank=True)
    TYPES = (('IMG', 'Image'), ('VID', 'Video'), ('DOC', 'Document'))
    video_url = models.URLField(max_length=200, null=True, blank=True)
    # file = models.FileField("uploads", null=True, blank=True)

    def __str__(self):
        return self.name


class Profession(MyAbstractModel):
    name = models.CharField(unique=True, max_length=50)
    personalities = models.ManyToManyField(Personality,null=True,blank=True)
    media=models.ManyToManyField(Media,null=True,blank=True)

    def __str__(self):
        return self.name



class Course(MyAbstractModel):
    name = models.CharField(max_length=100)
    profession = models.ForeignKey(Profession)
    university = models.ForeignKey(University)
    media = models.ManyToManyField(Media,null=True,blank=True)

    def __str__(self):
        return "{0}-{1}".format(self.university,self.name)


    class Meta:
        ordering=("id",)
        # unique_together=("name","")


class CourseCutoff(MyAbstractModel):
    course = models.ForeignKey(Course)
    points = models.FloatField()
    year = models.IntegerField()


    class Meta:
        ordering=("id",)
        unique_together=("year","course")


