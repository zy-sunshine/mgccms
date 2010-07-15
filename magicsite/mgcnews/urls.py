from django.conf.urls.defaults import *
#from django.conf import settings
import views

urlpatterns = patterns('')

urlpatterns += patterns('',
    url(r'^$', views.mgcnews_index, name='mgcnews_index'),
    url(r'^news_archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.mgcnews_index, name='mgcnews_month_archive'),
    url(r'^news_tags/(?P<tag>[-\w\.]+)/$', views.mgcnews_index, name='mgcnews_tags'),
    url(r'^post/(?P<username>[-\w]+)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug>[-\w]+)/$', 
        views.mgcnews_article, name='mgcnews_article'),
)
