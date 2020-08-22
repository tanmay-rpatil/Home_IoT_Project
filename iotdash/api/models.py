import datetime

from django.db import models
from django.utils import timezone

class LatestData(models.Model):
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    humidity = models.DecimalField(max_digits=4, decimal_places=2)
    timestamp = models.DateTimeField()