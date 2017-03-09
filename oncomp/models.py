from django.db import models

class prog_ques(models.Model):

   prog = models.TextField()
   pname = models.CharField(max_length=256)
   alotted_time = models.IntegerField()
   qno = models.IntegerField()
   mark=models.IntegerField()
   class Meta:
      db_table = "prog_ques"
   def __str__(self):
         return self.prog
class testcases(models.Model):
      test_cases=models.TextField(max_length=1000)
      test_out=models.TextField(max_length=1000, default='No Output')
      question_id=models.ForeignKey(prog_ques,on_delete=models.CASCADE)

class answer(models.Model):
      uid=models.CharField(max_length=256)
      tid=models.IntegerField()
      out=models.TextField()
      program=models.TextField()
      qno=models.IntegerField()
      language=models.IntegerField()
      class Meta:
            db_table="answer"