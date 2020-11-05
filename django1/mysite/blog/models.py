from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()

    def __str__(self):
        return self.name

class Catagory(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Articles(models.Model):
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    posted = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    body = models.TextField()
    catagory_name = models.ForeignKey(Catagory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title