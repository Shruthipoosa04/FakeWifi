from django.db import models

# Create your models here.
from django.db import models

class WiFiNetwork(models.Model):
    ssid = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=17, unique=True)
    signal_strength = models.IntegerField()
    is_suspicious = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ssid