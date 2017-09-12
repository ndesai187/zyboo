from django.shortcuts import render_to_response


def index():
    return render_to_response('zybooEvents/welcome.html')
