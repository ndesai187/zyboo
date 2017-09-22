from django.contrib.gis.db import models


class HappyPubs(models.Model):
    """
    Model for a registered locations
    """
    name = models.CharField(max_length=200)
    location = models.PointField()

    def __str__(self):
        return self.name


class PubEvent(models.Model):
    """
    Model for a Event @ locations
    """
    name = models.CharField(max_length=200)
    fromDatetime = models.DateTimeField()
    toDatetime = models.DateTimeField()
    pubName = models.ForeignKey(HappyPubs)

    def __str__(self):
        return "%s - %s" % (self.name, self.pubName.name)


class RegisteredPubs(models.Model):
    """
    Model for a registered locations
    """
    name = models.CharField(max_length=64)
    location = models.PointField()
    address_street_num = models.IntegerField()
    address_street_name = models.TextField(max_length=64)
    address_line2 = models.TextField(max_length=128)
    address_city = models.CharField(max_length=64)
    address_state = models.CharField(max_length=64)
    address_zipcode = models.CharField(max_length=16)
    address_country = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Events(models.Model):
    """
    Model for event registration
    """
    name = models.CharField(max_length=128)
    fromDatetime = models.DateTimeField()
    toDatetime = models.DateTimeField()
    addPromo = models.CharField(max_length=128)
    pubName = models.ForeignKey(RegisteredPubs)

    def __str__(self):
        return "%s - %s" % (self.name, self.pubName.name)


#link to Google API to get working days and workng hours