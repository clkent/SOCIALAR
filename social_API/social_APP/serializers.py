from rest_framework import serializers
from . import models


class SocialGeoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.SocialGeo
        fields = '__all__'