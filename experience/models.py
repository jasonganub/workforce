from django.db import models


class Experience(models.Model):
    applicant = models.ForeignKey(
        'Applicant',
        on_delete=models.CASCADE,
    )
    category = (
        (education, 'Education'),
        (work, 'Work'),
    )
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.CharField()
    institution = models.CharField()
