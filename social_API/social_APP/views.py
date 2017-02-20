from django.shortcuts import render
from rest_framework import generics

from . import serializers
from . import models 


class ListGeoData(generics.ListCreateAPIView):
    """Add documentation for endpoint use here"""
    queryset = models.SocialGeo.objects.all()
    serializer_class = serializers.SocialGeoSerializer


