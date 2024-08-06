from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)


class Rece(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    rname = models.CharField(max_length=100)
    rdesc = models.TextField()
    rimg = models.ImageField(upload_to="recipe")



class StudentId(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id
    
class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    class Meta:
        ordering = ['department']

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

class Student(models.Model):
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentId, related_name="studentid", on_delete=models.SET_NULL, null=True)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()
    is_deleted = models.BooleanField(default=False)


    objects = StudentManager()
    admin_object = models.Manager()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "student"

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student,related_name="subjectmarks",on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.student.student_name} {self.subject.subject_name}"

    class Meta:
        unique_together = ['student','subject']


class StudentRank(models.Model):
    student = models.ForeignKey(Student,related_name="studentmarks",on_delete=models.CASCADE)
    student_rank = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['student_rank','date']