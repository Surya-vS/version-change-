from django.db import models

# Create your models here.
# Create Student details:student name,rollno,branch
class Student(models.Model):
    stname=models.TextField()
    srollno=models.IntegerField()
    sbranch=models.IntegerField()
    sbloodgroup=models.TextField()


