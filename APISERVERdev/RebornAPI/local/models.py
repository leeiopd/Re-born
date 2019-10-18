from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=30)
    gun = models.ForeignKey('Gun', on_delete=models.CASCADE)

class Gun(models.Model):
    name = models.CharField(max_length=50)
    gu = models.ForeignKey('Gu', on_delete=models.CASCADE)

class Gu(models.Model):
    name = models.CharField(max_length=50)
    dong = models.ForeignKey('Dong', on_delete=models.CASCADE)

class Dong(models.Model):
    name = models.CharField(max_length=50)