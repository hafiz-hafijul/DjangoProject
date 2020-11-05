from django.db import models


class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length = 50)
    stuemail = models.EmailField(max_length = 50)
    stupass = models.CharField(max_length = 50)

    def __str__(self):
        return self.stuname