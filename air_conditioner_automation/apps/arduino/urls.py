from django.conf.urls import url, include
from rest_framework import routers

from air_conditioner_automation.apps.arduino import views as arduino_views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'device', arduino_views.ArduinoViewSet, 'device')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = router.urls
