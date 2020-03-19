from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    std_number = models.IntegerField()

    TEACHER = (
        ("razavizadeh", "Razavizadeh"),
        ("vakili", "Vakili"),
        ("beheshti", "Beheshti")
    )
    teacher = models.CharField(max_length=12, choices=TEACHER)
