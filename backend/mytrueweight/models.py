from django.conf import settings
from django.db import models


class Weight(models.Model):
    "Generated Model"
    weightId = models.UUIDField()
    date = models.DateTimeField(
        null=True,
        blank=True,
    )
    coffeeDrank = models.DecimalField(
        null=True,
        blank=True,
        max_digits=30,
        decimal_places=2,
    )
    afterEgestion = models.DecimalField(
        null=True,
        blank=True,
        max_digits=30,
        decimal_places=2,
    )
    mytrueweight = models.DecimalField(
        null=True,
        blank=True,
        max_digits=30,
        decimal_places=2,
    )


# Create your models here.
