# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from mylib.my_common import MyAbstractModel
from prediction.personality.models import Personality
from school.result.models import Result
from university.models import Course


class Prediction(MyAbstractModel):
    personality=models.ForeignKey(Personality)
    cluster_points=models.FloatField(null=True,blank=True)
    course=models.ForeignKey(Course,null=True,blank=True)
    result=models.ForeignKey(Result,null=True,blank=True)

    def __str__(self):
        return "%s-%s"%(self.course,self.course.university.name)