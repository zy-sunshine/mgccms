from django.conf.urls.defaults import *
#from django.conf import settings
import views

urlpatterns = patterns('')
urlpatterns += patterns('',
    url(r'^$', views.index, name='index'),
    
    url(r'^list_all_release/$', views.mgcindex_index, name='mgcindex_index'),
    url(r'^index_archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.mgcindex_index, name='mgcindex_month_archive'),
    url(r'^index_tags/(?P<tag>[-\w\.]+)/$', views.mgcindex_index, name='mgcindex_tags'),
    url(r'^post/(?P<username>[-\w]+)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug>[-\w]+)/$', 
        views.mgcindex_article, name='mgcindex_article'),
)
