from django.db import models

from client.models import MyUser
from mylib.my_common import MyAbstractModel


class Result(MyAbstractModel):
    type=(('I','Internal'),('M','Mock'),('K','KCSE'))
    year=models.IntegerField()
    user=models.ForeignKey(MyUser)
    avg_grade=models.CharField(max_length=2)
    avg_points=models.FloatField()
    type=models.CharField(choices=type,default='I',max_length=2)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return "%s %s-%s" %(self.user.firstname,self.year,self.avg_grade)






