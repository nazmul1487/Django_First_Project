from django.db import models


class StudentInfo(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=20)
    session = models.CharField(max_length=50)

