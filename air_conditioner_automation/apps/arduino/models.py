from collections import namedtuple
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from air_conditioner_automation.apps.common.models import DateTimeModel

# Create your models here.


class Arduino(DateTimeModel):
    """
    Represent a Arduino device
    """
    STATUS = namedtuple(u'Status', [u'ON', u'OFF'])(
        ON=1,
        OFF=2
    )
    STATUS_CHOICES = (
        (STATUS.ON, u'On'),
        (STATUS.OFF, u'Off')
    )

    mac_address = models.CharField(max_length=12, unique=True)
    ip_address = models.GenericIPAddressField(null=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=STATUS.OFF)
    temperature = models.PositiveSmallIntegerField(validators=[MinValueValidator(16), MaxValueValidator(30)], default=16)

    def __str__(self):
        return self.mac_address
