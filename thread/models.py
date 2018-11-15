from django.db import models
import threading

# Create your models here.

class ThreadTask(models.Model):
    task = models.CharField(max_length=30, blank=True, null=True)
    is_done = models.BooleanField(blank=False,default=False )
