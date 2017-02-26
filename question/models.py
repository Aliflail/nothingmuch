from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.
class Apt_Test(models.Model):
   time = models.DurationField()
   name = models.CharField(max_length=100)
   startDate = models.DateField(default=datetime.now, blank=True)
   endDate = models.DateField(default=datetime.now, blank=True)

   def __str__(self):
       return self.name

class Apt_Qns(models.Model):
    question = models.TextField()
    test_id = models.ForeignKey(Apt_Test,on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class Options(models.Model):
    option = models.CharField(max_length=300)
    qn_id = models.ForeignKey(Apt_Qns,on_delete=models.CASCADE)

    def __str__(self):
        return self.option

class Answers(models.Model):
    answer = models.CharField(max_length=300)
    qn_id = models.ForeignKey(Apt_Qns,on_delete=models.CASCADE)

    def __str__(self):
        return self.answer
