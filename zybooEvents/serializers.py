from rest_framework import serializers
from .models import PubEvent, HappyPubs


class PubEventSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = PubEvent
        fields = '__all__'
        # fields = ('id','name','fromDatetime','toDatetime')
        # fields = ('id', 'name')


class HappyPubsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = HappyPubs
        fields = '__all__'
