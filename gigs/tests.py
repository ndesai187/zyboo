from django.test import TestCase
from gigs.models import HappyPubs
from factory.fuzzy import BaseFuzzyAttribute
from django.contrib.gis.geos import Point
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
        print("This is only_venue variable : " + only_venue.name)
        print("This is all_venue objects : ")
        print(only_venue.location)
        print("This is Meta object location : ")
        print(pub.location)
        self.assertEqual(only_venue.name, 'Petty Pub')


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