from django.db import models
from django.utils import timezone

class Person(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    sex = models.CharField(max_length=6,default="Female")
    age = models.IntegerField(default=0)
    
    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)
