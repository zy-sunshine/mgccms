from django.conf.urls.defaults import *
#from django.conf import settings
import views

urlpatterns = patterns('')

urlpatterns += patterns('',
    url(r'^$', views.mgcprojects_index, name='mgcprojects_index'),
    url(r'^projects_archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.mgcprojects_index, name='mgcprojects_month_archive'),
    url(r'^projects_tags/(?P<tag>[-\w\.]+)/$', views.mgcprojects_index, name='mgcprojects_tags'),
    url(r'^post/(?P<username>[-\w]+)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug>[-\w]+)/$', 
        views.mgcprojects_article, name='mgcprojects_article'),
)
