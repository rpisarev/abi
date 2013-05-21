from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django import template
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, get_list_or_404
from django.template.context import RequestContext
from django.views.generic.base import RedirectView
from django.utils import translation
import abi.settings
from event.models import *
from abinito.models import *
from abinito.views import change_lang

sufix = 'event/'
four = 4

def event(request, idn):
    try:
        record = EventRecord.objects.get(id = idn)
    except:
        record = EventRecord.objects.all()[0]
        idn = record.id

    '''Site must have one or more EventRecord '''

    if record.report:
        event_template = 'event_report.html'
    else:
        event_template = 'event_anounce.html'
    return render_to_response(event_template,
        {
            'backgr': MainMenuItem.objects.get(url = sufix),
            'mainmenu': MainMenuItem.objects.all().exclude(url = '/'),
            'lang': change_lang(request),
            'event': EventRecord.objects.get(id = idn),
            'socnets': SocNet.objects.all(),
            'lasts': EventRecord.objects.all().order_by('id')[:four],
            'anon': EventRecord.objects.all().order_by('-id')[:1][0].id,
            'photo': EventRecord.objects.all().filter(report = True).order_by('-id')[:1][0].id,
        }
    )
