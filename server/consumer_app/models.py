from datetime import date

from django.db import models

from .constants import SENSEHAT_SENSORS, SENSEHAT_SOURCE


# ==============================================================================
class SensehatReading(models.Model):
    # We make sure there is a one2one relationship with the user model
    created = models.DateTimeField(auto_now_add=True)

    sensehat_sensor = models.IntegerField(choices=SENSEHAT_SENSORS, default=0)
    reading = models.CharField(max_length=10, null=False, blank=False)
    source = models.IntegerField(choices=SENSEHAT_SOURCE)

    def __str__(self):
        return str(self.id)
