from django.db import models


class Applicant(models.Model):
    job = models.ForeignKey(
        'Job',
        on_delete=models.CASCADE,
    )
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.CharField()
    status = (
        (under_review, 'Under review'),
        (rejected, 'Rejected'),
        (offer_pending, 'Offer pending'),
        (offer_accepted, 'Offer accepted - yet to start'),
        (started, 'Started'),
    )
