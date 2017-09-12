from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from zybooEvents.views import LookupView, GetPubEventJson, GetHappyPubsJson, WelcomeView

urlpatterns = [
    #Lookup
    url(r'^$', WelcomeView.as_view(), name='welcome'),
    url(r'^findpub/$',LookupView.as_view(),name='lookup'),
    url(r'^evesJson/$', GetPubEventJson.as_view(), name='EventList'),
    url(r'^pubsJson/$', GetHappyPubsJson.as_view(), name='pubList')
]

urlpatterns = format_suffix_patterns(urlpatterns)