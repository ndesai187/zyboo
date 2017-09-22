from django.shortcuts import render_to_response, render
from django.views.generic.edit import FormView
from rest_framework.response import Response
from zybooEvents.forms import LookupForm
from zybooEvents.models import PubEvent, HappyPubs, RegisteredPubs, Events
from django.utils import timezone
from django.contrib.gis.geos import Point
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
    def get(self, request):
        lat = request.GET.get('lat')
        long = request.GET.get('long')
        lat1 = int(lat) + 5
        long1 = int(long) + 30
        # temp = TempClass(lat=lat, long=long, *args, **kwargs)
        temp = [{"lat": lat, "long": long}, {"lat": lat1, "long": long1}]
        serialized_temp = TestSerializer(temp, many=True)
        # return HttpResponse(serialized.data, content_type="application/json")
        return Response(serialized_temp.data)
