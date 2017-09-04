from django.shortcuts import render_to_response, render
from django.views.generic.edit import FormView
from gigs.forms import LookupForm
from gigs.models import PubEvent
from django.utils import timezone
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.template import Context, RequestContext


class LookupView(FormView):
    form_class = LookupForm

    def get(self, request):
        #context = {}
        # render_to_response is obsolete.
        # return render_to_response('gigs/lookup.html', context_instance=RequestContext(request))
        return render(request, 'gigs/lookup.html')

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

        return render_to_response('gigs/lookupresults.html', {
            'events': events
        })
