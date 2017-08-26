from rest_framework import serializers

from air_conditioner_automation.apps.arduino import models as arduino_models


# Serializers define the API representation.
class ArduinoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = arduino_models.Arduino
        fields = ('id', 'mac_address', 'ip_address', 'status', u'temperature')
