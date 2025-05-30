from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} - {self.title}"

class Student(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


# Create your models here.
