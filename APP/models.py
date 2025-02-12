from django.db import models

# Create your models here.

# https://metanit.com/python/django/5.1.php
class pc(models.Model):
    hostname = models.CharField(max_length=20)
    ip = models.CharField(max_length=15)
    users = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)