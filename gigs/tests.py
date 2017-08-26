from django.test import TestCase
from gigs.models import HappyPubs, PubEvent
from factory.fuzzy import BaseFuzzyAttribute
from django.contrib.gis.geos import Point
import factory.django, random
from django.utils import timezone

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


        #exclude = ('naming','location')
        #abstract = False
        #inline_args = ('name', 'location')#model.naming = 'Petty Pub'
        #model.location = FuzzyPoint()
        #naming = 'Petty pub'
        #location = FuzzyPoint()
        #class Params:
        #    id = factory.Sequence(lambda n: n)
        #    naming = 'Petty Pub'
        #    location = FuzzyPoint()
        #    print("variable initialized")