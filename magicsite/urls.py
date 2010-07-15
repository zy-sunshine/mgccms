from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template

#from magicsite.mgccms.views import about_pages

admin.autodiscover()

urlpatterns = patterns('')

if getattr(settings, 'TINYMCE_FILEBROWSER', False):
    urlpatterns += patterns('',
        url(r'^admin/filebrowser/', include('filebrowser.urls')),
    )

urlpatterns += patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    
    #(r'^accounts/profile/$',  profile),


    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^about\.html$', direct_to_template, {
        'template': 'about.html'
    }),
    
    # Fix ...
    #url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
    #    {'feed_dict': feeds}, name='dpress_feeds'),

)
urlpatterns += patterns('',
    url('^'+settings.SITE_CONFIG['index_url'][1:], include('mgcindex.urls')),
    url('^'+settings.SITE_CONFIG['news_url'][1:], include('mgcnews.urls')),
    url('^'+settings.SITE_CONFIG['projects_url'][1:], include('mgcprojects.urls')),
    url('^'+settings.SITE_CONFIG['accounts_url'][1:], include('mgcaccounts.urls')),
)


urlpatterns += patterns('',
    url(r'^tinymce/', include('tinymce.urls')),
    (r'^attachments/', include('attachments.urls')),
)


    