# Create your views here.
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django import template
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, get_list_or_404
from django.template.context import RequestContext
from django.utils import translation
import abi.settings
from portfolio.models import *
from abinito.models import *
from event.models import *

RowNumber = 5
portfolio_sufix = 'portfolio'
four = 3

def five_last_post(number = RowNumber):
    return PortfRecord.objects.all().order_by('-created')[:number]

def categorys_in_row(without_category, number_in_row = RowNumber - 1):
    categ = PortfCateg.objects.all().exclude(name_in_uri = without_category)
    res = []
    for row in xrange(0, len(categ) // number_in_row + 1):
        res += [categ[row:row + number_in_row]]
    return res

from abinito.views import change_lang, set_lang
def portf_index(request):
    request = set_lang(request)
    return render_to_response('index_portfolio.html',
        {
            'lastposts': five_last_post(),
            'categorys': PortfCateg.objects.all(),
            'backgr': MainMenuItem.objects.get(url = portfolio_sufix),
            'mainmenu': MainMenuItem.objects.all().exclude(url = '/'),
            'lang': change_lang(request),
            'lasts': EventRecord.objects.all().order_by('id')[:four],
        }
    )

def portf_categ_list(request, categ):
    request = set_lang(request)
    return render_to_response('category_portfolio.html',
        {
            'lastposts': five_last_post(),
            'categ': PortfCateg.objects.get(name_in_uri = categ),
            'categ_down': categorys_in_row(categ),
            'backgr': MainMenuItem.objects.get(url = portfolio_sufix),
            'mainmenu': MainMenuItem.objects.all().exclude(url = '/'),
            'lang': change_lang(request),
            'lasts': EventRecord.objects.all().order_by('id')[:four],
        }
    )

def portf_item(request, portf):
    request = set_lang(request)
    project = PortfRecord.objects.get(url = portf)
    return render_to_response('project_portfolio.html',
        {
            'lastposts': five_last_post(),
            'categ_down': categorys_in_row(project.category.name_in_uri),
            'portfolio': project,
            'backgr': MainMenuItem.objects.get(url = portfolio_sufix),
            'mainmenu': MainMenuItem.objects.all().exclude(url = '/'),
            'lang': change_lang(request),
            'lasts': EventRecord.objects.all().order_by('id')[:four],
        }
    )
