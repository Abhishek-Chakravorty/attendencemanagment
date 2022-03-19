from django.db import models

# Create your models here.
class Faculty_Registration(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    qual = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Student_DB(models.Model):
    sno =models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    rollno = models.IntegerField()
    course = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

class Attendence_record(models.Model):
    rollno = models.IntegerField()
    date =  models.DateField()
    faculty = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default='Absent')