from django.contrib import admin
from zybooEvents.models import HappyPubs, PubEvent, RegisteredPubs, Events
from django.forms import ModelForm
from floppyforms.gis import PointWidget, BaseGMapWidget


class CustomPointWidget(PointWidget, BaseGMapWidget):
    class Media:
        js = ('/static/floppyforms/js/MapWidget.js',)


class HappyPubAdminForm(ModelForm):
    class Meta:
        model = HappyPubs
        fields = ['name', 'location']
        widgets = {
            'location': CustomPointWidget()
        }


class HappyPubAdmin(admin.ModelAdmin):
    form = HappyPubAdminForm


class RegPubAdminForm(ModelForm):
    class Meta:
        model = RegisteredPubs
        fields = ['name', 'address_street_num',
                  'address_street_name', 'address_line2',
                  'address_city', 'address_state',
                  'address_zipcode', 'address_country', 'location']
        widgets = {
            'location': CustomPointWidget()
        }


class RegPubAdmin(admin.ModelAdmin):
    form = RegPubAdminForm


# Register your models here.
admin.site.register(HappyPubs, HappyPubAdmin)
admin.site.register(PubEvent)
admin.site.register(RegisteredPubs, RegPubAdmin)
admin.site.register(Events)
