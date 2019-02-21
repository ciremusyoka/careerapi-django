from django.db import models

from mylib.my_common import MyAbstractModel


class Personality(MyAbstractModel):
    name=models.CharField(max_length=45,unique=True)

    def __str__(self):
        return self.name