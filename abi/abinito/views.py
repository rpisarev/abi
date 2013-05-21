# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django import template
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, get_list_or_404
from django.template.context import RequestContext
import abi.settings
from django.utils import translation
from abinito.models import *
from event.models import *
import string

four = 3

def simplepage(sufix, switcher):
    '''Rendering simple page'''
    return render_to_response('simple_page.html',
        {
            'page': MainMenuPage.objects.get(item__url = sufix),
            'backgr': MainMenuItem.objects.get(url = sufix),
            'mainmenu': MainMenuItem.objects.all().exclude(url = '/'),
            'lang': switcher,
            'lasts': EventRecord.objects.all().order_by('id')[:four],
        }
    )

def change_lang(request):
    '''Return tuple (url, caption, current_lang)'''
    lang = {
    u'ru': u'en',
    u'en': u'ru',
    }
    trans = {
    u'ru': u'In English',
    u'en': u'Русский',
    }
    url = request.META['PATH_INFO'].split('/')
    return ('/' + lang[url[1]] + '/' + '/'.join(url[2:]), trans[url[1]], url[1])

def set_lang(request):

    '''Set 'django_language' in request.session'''

    url = request.META['PATH_INFO'].split('/')[1]
    request.session['django_language'] = url
    return request

from portfolio.views import five_last_post

def serv(request):
    sufix = 'services/'
    switcher = change_lang(request)
    return simplepage(sufix, switcher)

def con(request):
    sufix = 'contacts/'
    switcher = change_lang(request)
    return simplepage(sufix, switcher)

def indexpage(request):
    sufix = '/'
    switcher = change_lang(request)
    return render_to_response('main_page.html',
        {
            'lastposts': five_last_post(),
            'news': '',
            'events':'',
            'backgr': MainMenuItem.objects.get(url = sufix),
            'mainmenu': MainMenuItem.objects.all().exclude(url = '/'),
            'lang': switcher,
            'lasts': EventRecord.objects.all().order_by('id')[:four],
        }
    )
