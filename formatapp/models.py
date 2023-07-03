from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Auditorium(models.Model):
    day = models.DateField()
    time = models.CharField(max_length=50)
    eventType = models.CharField(max_length=50)
    describe = models.TextField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.PROTECT,null=True)
    def __str__(self):
        return f"{self.day} | {self.time}"
    

class Amphitheatre(models.Model):
    day = models.DateField()
    time = models.CharField(max_length=50)
    eventType = models.CharField(max_length=50)
    describe = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT,null=True)
    def __str__(self):
        return f"{self.day} | {self.time}"
    

class SeminarHall(models.Model):
    day = models.DateField()
    time = models.CharField(max_length=50)
    eventType = models.CharField(max_length=50)
    describe = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT,null=True)
    def __str__(self):
        return f"{self.day} | {self.time}"


class SportsGround(models.Model):
    day = models.DateField()
    time = models.CharField(max_length=50)
    eventType = models.CharField(max_length=50)
    describe = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT,null=True)
    def __str__(self):
        return f"{self.day} | {self.time}"
    



