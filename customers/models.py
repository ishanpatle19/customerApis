from django.db import models

# Create your models here.
from django.db import models


class Customer(models.Model):
    firstName = models.CharField(blank=False, max_length=50, default='')
    lastName = models.CharField(blank=False, max_length=50, default='')
    email = models.CharField(max_length=70, blank=False, default='')
    password = models.IntegerField(blank=False, default=25)
    phone = models.CharField(blank=False, max_length=50)


class Register(models.Model):
    firstName = models.CharField(blank=False, max_length=50, default='')
    lastName = models.CharField(blank=False, max_length=50, default='')
    email = models.CharField(max_length=70, blank=False, default='')
    password = models.IntegerField(blank=False, default=25)
    phone = models.CharField(blank=False, max_length=50)

class Login(models.Model):
    email = models.CharField(max_length=70, blank=False, default='')
    password = models.IntegerField(blank=False, default=25)

class Forgot(models.Model):
    email = models.CharField(max_length=70, blank=False, default='')



