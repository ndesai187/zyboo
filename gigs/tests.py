from django.test import TestCase, RequestFactory
from gigs.models import HappyPubs, PubEvent
from factory.fuzzy import BaseFuzzyAttribute
from django.contrib.gis.geos import Point
from django.utils import timezone
from django.core.urlresolvers import reverse
from gigs.views import LookupView
from rest_framework.test import APIClient
from rest_framework import status

import factory.django, random


class FuzzyPoint(BaseFuzzyAttribute):
    def fuzz(self):
        return Point(random.uniform(-180.0, 180.0),
                     random.uniform(-90.0, 90.0))

#Factories for tests
class HappyPubFactory(factory.django.DjangoModelFactory):
    name = 'Petty Pub'
    location = FuzzyPoint()
    class Meta:
        model = HappyPubs
        django_get_or_create = ('name', 'location', )

class PubEventFactory(factory.django.DjangoModelFactory):
    name = 'Happy Hours'
    fromDatetime = timezone.now()
    toDatetime = timezone.now()
    class Meta:
        model = PubEvent
        django_get_or_create = ('name', 'fromDatetime', 'toDatetime', 'pubName', )

class PubTest(TestCase):
    def test_create_venue(self):
        #create the place
        pub = HappyPubFactory()

        #Check if we can search
        all_venues = HappyPubs.objects.all()
        self.assertEqual(len(all_venues),1)
        only_venue = all_venues[0]
        self.assertEqual(only_venue,pub)

        #Check Attributes
        print("\n------------------------")
        print("-- Running Pub Test")
        print("------------------------")
        print("This is only_venue variable : " + only_venue.name)
        print("This is all_venue objects : ")
        print(only_venue.location)
        print("This is Meta object location : ")
        print(pub.location)
        self.assertEqual(only_venue.name, 'Petty Pub')

        #Check String representation
        self.assertEqual(only_venue.__str__(),'Petty Pub')

class EventTest(TestCase):
    def test_create_venue(self):

        #create the pub
        pub = HappyPubFactory()

        #create the happy hour event
        event = PubEventFactory(pubName=pub)

        #Check if we can search
        all_events = PubEvent.objects.all()
        self.assertEqual(len(all_events),1)
        only_event = all_events[0]
        self.assertEqual(only_event,event)

        #Check Attributes
        print("------------------------")
        print("-- Running Event Test")
        print("------------------------")
        print("This is only_event variable : " + only_event.name)
        print("This is only_event location : ")
        print(only_event.pubName.location)
        print("This is Meta object location : ")
        print(pub.location)
        print("This is Event start time : " + str(only_event.fromDatetime))
        self.assertEqual(only_event.name, 'Happy Hours')
        self.assertEqual(only_event.pubName.name, 'Petty Pub')

        #Check String representation
        self.assertEqual(only_event.__str__(),'Happy Hours - Petty Pub')


class LookupViewTest(TestCase):
    """
    Test lookup view
    """
    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        p1 = HappyPubFactory(name='Pub1')
        p2 = HappyPubFactory(name='Pub2')
        p3 = HappyPubFactory(name='Pub3')
        p4 = HappyPubFactory(name='Pub4')
        p5 = HappyPubFactory(name='Pub5')
        p6 = HappyPubFactory(name='Pub6')

        e1 = PubEventFactory(name='Event1',pubName=p1)
        e2 = PubEventFactory(name='Event2',pubName=p2)
        e3 = PubEventFactory(name='Event3',pubName=p3)
        e4 = PubEventFactory(name='Event4',pubName=p4)
        e5 = PubEventFactory(name='Event5',pubName=p5)
        e6 = PubEventFactory(name='Event6',pubName=p6)

        # Set parameters
        lat = 52.3749159
        lon = 1.1067473
        # Put together request

        data = {
            'latitude': lat,
            'longitude': lon
        }

        request = self.factory.post(reverse('lookup'),data)
        response = LookupView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('gigs/lookupresults.html')

#class ViewPubEventApi(TestCase):
#    """Test suite for the api views."""

#    def setUp(self):
#        """Define the test client and other test variables."""
#        self.client = APIClient()
