from django.db import models

from client.models import MyUser
from mylib.my_common import MyAbstractModel
from school.models import Subject
from school.result.models import Result


class SubjectResult(MyAbstractModel):
    subject=models.ForeignKey(Subject)
    result=models.ForeignKey(Result)
    grade=models.CharField(max_length=2)
    points=models.IntegerField()

    class Meta:
        ordering = ("id",)
        unique_together=("result","subject")

    def __str__(self):
        return "%s-%s"%(self.subject.name,self.grade)