from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
