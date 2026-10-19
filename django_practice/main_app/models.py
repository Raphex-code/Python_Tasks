from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.IntegerField(primary_key=True)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()

    class Meta:
        db_table = 'students'


    def __str__(self):
         return self.name
