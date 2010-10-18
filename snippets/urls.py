from django.conf.urls.defaults import *

urlpatterns = patterns('boundless.django.snippets.views',
    url(r'^$', 'index', name='snippet_index'),
    url(r'^(?P<page>[\d+])/$', 'index', name='snippet_index'),
    url(r'^snippet/(?P<identifier>[\d]+)/$','snippet',name='snippet_detail'),
    url(r'^snippet/(?P<identifier>[^/]+)/$','snippet',{'slugified':True},name='snippet_detail'),
)

