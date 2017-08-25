import requests

from django.conf import settings
from rest_framework import viewsets

from air_conditioner_automation.apps.arduino import (
    models as arduino_models,
    serializers as arduino_serializers
)


# ViewSets define the view behavior.
class ArduinoViewSet(viewsets.ModelViewSet):
    queryset = arduino_models.Arduino.objects.all()
    serializer_class = arduino_serializers.ArduinoSerializer

    def perform_update(self, serializer):
        super(ArduinoViewSet, self).perform_update(serializer)
        device = self.get_object()
        requests.get(u'{0}://{1}:{2}'.format(settings.ARDUINO_PROTOCOL, device.ip_address, settings.ARDUINO_PORT))