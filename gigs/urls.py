from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from gigs.views import LookupView, GetPubEventJson, GetHappyPubsJson

urlpatterns = [
    #Lookup
    url(r'^findgig/$',LookupView.as_view(),name='lookup'),
    url(r'^evesJson/$', GetPubEventJson.as_view(), name='EventList'),
    url(r'^pubsJson/$', GetHappyPubsJson.as_view(), name='pubList')
]

urlpatterns = format_suffix_patterns(urlpatterns)