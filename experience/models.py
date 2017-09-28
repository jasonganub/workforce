from django.db import models
from applicant.models import Applicant


class Experience(models.Model):
    EDUCATION = 'E'
    WORK = 'W'
    CATEGORY_CHOICES = (
        (EDUCATION, 'Education'),
        (WORK, 'Work'),
    )

    applicant = models.ForeignKey(
        Applicant,
        on_delete=models.CASCADE,
    )
    category = models.CharField(
        max_length=1,
        choices=CATEGORY_CHOICES,
    )
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.CharField(max_length=200)
    institution = models.CharField(max_length=50)
