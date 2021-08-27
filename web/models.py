from django.db import models
import uuid

# Create your models here.
class Language(models.Model):
    id = models.UUIDField(uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    



class Signup(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    tel = models.IntegerField()
    username = models.CharField(max_length=30, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(uuid.uuid4, unique=True, primary_key=True)

    def __str__(self):
        return self.username

class Projects(models.Model):
    id = models.UUIDField(uuid.uuid4, unique=True, primary_key=True)
    title = models.CharField(max_length=40)
    language = models.ManyToManyField(Language)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
