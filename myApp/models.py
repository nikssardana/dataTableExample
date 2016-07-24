from __future__ import unicode_literals

from django.db import models

class studentRecord(models.Model):
    roll = models.IntegerField(unique=True)
    Name = models.CharField(max_length = 50)
    section = models.CharField(max_length = 20)
