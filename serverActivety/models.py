from django.db import models

# Create your models here.
class Time(models.Model):
    uptime = models.IntegerField(default=0)
    noPlayerTime = models.IntegerField(default=0)
    date = models.DateField()
