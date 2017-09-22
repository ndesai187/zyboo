from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from zybooEvents.views import LookupView, GetPubEventJson, GetHappyPubsJson, \
    WelcomeView, GetRegPubsJson, GetEventsJson, GetQueryParam

urlpatterns = [
    # Lookup
    url(r'^$', WelcomeView.as_view(), name='welcome'),
    url(r'^findpub/$',LookupView.as_view(),name='lookup'),
    # url(r'^evesJson/$', GetPubEventJson.as_view(), name='EventList'),
    # url(r'^pubsJson/$', GetHappyPubsJson.as_view(), name='pubList'),
    url(r'^pubJson/$', GetRegPubsJson.as_view(), name='RegPubList'),
    url(r'^evesJson/$', GetEventsJson.as_view(), name='Events_List'),
    url(r'^query$', GetQueryParam.as_view(), name='query_param'),
]

urlpatterns = format_suffix_patterns(urlpatterns)