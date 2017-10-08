from django.shortcuts import render_to_response, render
from django.views.generic.edit import FormView
from rest_framework.response import Response
from zybooEvents.forms import LookupForm
from zybooEvents.models import PubEvent, HappyPubs, RegisteredPubs, Events
from django.utils import timezone
from django.contrib.gis.geos import Point
# from django.contrib.gis.geoip2 import GeoIP2
from django.contrib.gis.db.models.functions import Distance
from .serializers import PubEventSerializer, HappyPubsSerializer, \
    EventSerializer, RegPubsSerializer, TestSerializer
from rest_framework import generics, views


class WelcomeView(FormView):
    def get(self, request):
        return render(request, 'zybooEvents/welcome.html')


class LookupView(FormView):
    form_class = LookupForm

    def get(self, request):
        # context = {}
        # render_to_response is obsolete.
        # return render_to_response('zybooEvents/lookup.html', context_instance=RequestContext(request))
        return render(request, 'zybooEvents/lookup.html')

    def form_valid(self, form):
        # Get Data
        latitude = form.cleaned_data['latitude']
        longitude = form.cleaned_data['longitude']

        # Get today's date
        now = timezone.now()

        # Get next week's date
        next_week = now + timezone.timedelta(weeks=1)

        # Get Point
        location = Point(longitude, latitude, srid=4326)

        # Look up Events
        events = PubEvent.objects.filter(fromDatetime__gte=now).filter(fromDatetime__lte=next_week).annotate(
            distance=Distance('pubName__location', location)).order_by('distance')[0:5]

        # Render the template

        return render_to_response('zybooEvents/lookupresults.html', {
            'events': events
        })


class GetPubEventJson(generics.ListCreateAPIView):
    queryset = PubEvent.objects.all()
    serializer_class = PubEventSerializer

    def list(self, request):
        queryset = PubEvent.objects.all()
        serialized_eve = PubEventSerializer(queryset, many=True)
        # return HttpResponse(serialized.data, content_type="application/json")
        return Response(serialized_eve.data)


class GetHappyPubsJson(generics.ListCreateAPIView):
    queryset = HappyPubs.objects.all()
    serializer_class = HappyPubsSerializer

    def list(self, request):
        queryset = HappyPubs.objects.all()
        serialized_pub = HappyPubsSerializer(queryset, many=True)
        # return HttpResponse(serialized.data, content_type="application/json")
        return Response(serialized_pub.data)


class GetEventsJson(generics.ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer

    def list(self, request):
        queryset = Events.objects.all()
        serialized_eve = EventSerializer(queryset, many=True)
        # return HttpResponse(serialized.data, content_type="application/json")
        return Response(serialized_eve.data)


class GetRegPubsJson(generics.ListCreateAPIView):
    queryset = RegisteredPubs.objects.all()
    serializer_class = RegPubsSerializer

    def list(self, request):
        queryset = RegisteredPubs.objects.all()
        serialized_pub = RegPubsSerializer(queryset, many=True)
        # return HttpResponse(serialized.data, content_type="application/json")
        return Response(serialized_pub.data)


class GetQueryParam(views.APIView):
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    # def get_country(self,request):
        # g = GeoIP2()
        # country_code = g.country_code(self.get_client_ip(request))
        # lat, long = g.lat_lon('google.com')
        # return ">>country code is : " + country_code + " >>latitude is : " + str(lat) + " >>longitude is : " + str(long)

    def get(self, request):
        lat = request.GET.get('lat')
        long = request.GET.get('long')
        ipaddr = self.get_country(request)
        lat1 = int(lat) + 5
        long1 = int(long) + 30
        # temp = TempClass(lat=lat, long=long, *args, **kwargs)
        temp = [{"lat": lat, "long": long, "ip": ipaddr}, {"lat": lat1, "long": long1, "ip": ipaddr}]
        serialized_temp = TestSerializer(temp, many=True)
        # return HttpResponse(serialized.data, content_type="application/json")
        return Response(serialized_temp.data)
