from django.db import models
from job.models import Job


class Applicant(models.Model):
    UNDER_REVIEW = 'UR'
    REJECTED = 'REJ'
    OFFER_PENDING = 'OP'
    OFFER_ACCEPTED = 'OA'
    STARTED = 'ST'
    STATUS_CHOICES = (
        (UNDER_REVIEW, 'Under review'),
        (REJECTED, 'Rejected'),
        (OFFER_PENDING, 'Offer pending'),
        (OFFER_ACCEPTED, 'Offer accepted - yet to start'),
        (STARTED, 'Started'),
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
    )
