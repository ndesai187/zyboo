from rest_framework import serializers
from .models import PubEvent, HappyPubs, RegisteredPubs, Events


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


class EventSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Events
        fields = '__all__'
        # fields = ('id','name','fromDatetime','toDatetime')
        # fields = ('id', 'name')


class RegPubsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = RegisteredPubs
        fields = '__all__'


class TestSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    lat = serializers.IntegerField()
    long = serializers.IntegerField()
    ip = serializers.CharField()
