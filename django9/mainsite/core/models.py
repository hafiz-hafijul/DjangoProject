from django.db import models


class Student(models.Model):
    sduid = models.IntegerField()
    stuname = models.CharField(max_length=50)
    stuemail = models.EmailField(max_length=25)
    stupass = models.CharField(max_length=60)

    def __str__(self):
        return self.stuname
    