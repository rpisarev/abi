"""Urls for the demo of Zinnia"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls import patterns
from django.views.generic.base import RedirectView

from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap

from django.conf.urls import patterns, include, url
from django.utils.translation import ugettext_lazy as _
from django.conf.urls.i18n import i18n_patterns

admin.autodiscover()
handler500 = 'abi.views.server_error'
handler404 = 'django.views.defaults.page_not_found'
handler403 = 'django.views.defaults.permission_denied'

urlpatterns = i18n_patterns(
    '',
    url(r'^$', RedirectView.as_view(url='/index/')),
    url(r'^blog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


import portfolio.views
urlpatterns += i18n_patterns('portfolio.views',
    url(r'^portfolio/$', 'portf_index', name = 'index_portf'),
    url(r'^portfolio/category/(\w+)/$', 'portf_categ_list', name = 'portf_categ'),
    url(r'^portfolio/(\w+)/$', 'portf_item', name = 'portf_one_item'),
)
import abinito.views
urlpatterns += i18n_patterns('abinito.views',
    url(r'^services/$', 'serv', name = 'index_portf'),
    url(r'^contacts/$', 'con', name = 'index_cont'),
    url(r'^index/$', 'indexpage', name = 'index_main'),
)

import event.views
from event.models import *
up_event = EventRecord.objects.all().order_by('-id')[:1][0].id
event_redirect = str(up_event) + '/'

urlpatterns += i18n_patterns('event.views',
    url(r'^event/$', RedirectView.as_view(url = event_redirect)),
    url(r'^event/(\d+)/$', 'event', name = 'event_anon'),
)


sitemaps = {
    'tags': TagSitemap,
    'blog': EntrySitemap,
    'authors': AuthorSitemap,
    'categories': CategorySitemap
}

urlpatterns += patterns(
    'django.contrib.sitemaps.views',
    url(r'^sitemap.xml$', 'index',
        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',
        {'sitemaps': sitemaps}),
)

urlpatterns += patterns(
    '',
    url(r'^403/$', 'django.views.defaults.permission_denied'),
    url(r'^404/$', 'django.views.defaults.page_not_found'),
    url(r'^500/$', 'abi.views.server_error'),
)



if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
	url(r'portfolio/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )