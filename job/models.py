from django.db import models


class Job(models.Model):
    title = models.CharField()
    location = models.CharField()
    description = models.CharField()
