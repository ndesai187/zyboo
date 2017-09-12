from django.shortcuts import render_to_response, render
from django.views.generic.edit import FormView
from rest_framework.response import Response
from zybooEvents.forms import LookupForm
from zybooEvents.models import PubEvent, HappyPubs
from django.utils import timezone
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .serializers import PubEventSerializer, HappyPubsSerializer
from rest_framework import generics


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