from rest_framework import serializers
from .models import WiFiNetwork

class WiFiNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = WiFiNetwork
        fields = '__all__'
