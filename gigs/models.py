from django.contrib.gis.db import models

class HappyPubs(models.Model):
    """
    Model for a registered locations
    """
    name = models.CharField(max_length=200)
    location = models.PointField()
