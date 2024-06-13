from django.db import models

# Create your models here.
from django.urls import reverse
class School(models.Model):
    school_name=models.CharField(max_length=30)
    school_principal=models.CharField(max_length=30)
    school_location=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.school_name
    

    def get_absolute_url(self):
        return reverse('SchoolDetail',kwargs={'pk':self.pk})



class Student(models.Model):
    student_name=models.CharField(max_length=30)
    student_age=models.IntegerField()
    school_name=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
    def __str__(self) -> str:
        return self.student_name
