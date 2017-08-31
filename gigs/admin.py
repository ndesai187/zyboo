from django.contrib import admin
from gigs.models import HappyPubs, PubEvent
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


# Register your models here.
admin.site.register(HappyPubs, HappyPubAdmin)
admin.site.register(PubEvent)
