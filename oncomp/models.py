from django.db import models
from accounts import models as ac_models
from django.conf import settings


class CodeTest(models.Model):
    TestName = models.CharField(max_length=250)

class prog_ques(models.Model):
    prog = models.TextField(default="")
    pname = models.CharField(max_length=256)
    alotted_time = models.DurationField()
    mark=models.IntegerField(default=0)
    TestId = models.ForeignKey(CodeTest,on_delete=models.CASCADE)
    def __str__(self):
         return self.prog

class testcases(models.Model):
    test_cases=models.TextField(max_length=1000)
    test_out=models.TextField(max_length=1000, default='No Output')
    question_id=models.ForeignKey(prog_ques,on_delete=models.CASCADE)
    def __str__(self):
        return self.test_out


class answer(models.Model):
    uid=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    tid=models.ForeignKey(CodeTest,on_delete=models.CASCADE)
    qid = models.ForeignKey()
    out=models.TextField(default="")
    program=models.TextField(default="")
    language=models.IntegerField(default=0)
    class Meta:
        db_table="answer"

    def __str__(self):
        return self.prog
