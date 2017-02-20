from django.db import models

class SocialGeo(models.Model):
    id = models.AutoField(primary_key=True)
    content_type = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()
    
    class Meta:
        db_table = 'social_geo'
