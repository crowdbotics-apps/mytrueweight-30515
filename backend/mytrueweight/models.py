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
        max_digits=30,
        decimal_places=2,
        null=True,
        blank=True,
    )
    afterEgestion = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        null=True,
        blank=True,
    )
    mytrueweight = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        null=True,
        blank=True,
    )


# Create your models here.
