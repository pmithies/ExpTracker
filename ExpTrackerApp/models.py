from django.db import models


class ExpTracker(models.Model):
    description = models.CharField(max_length=200)
    amount = models.IntegerField()