from django.conf.urls.defaults import *

import views

urlpatterns = patterns('')

urlpatterns += patterns('',

    #url(r'^$', views.mllogin, {'template_name': 'accounts/login.html'}),
    url(r'^register/$', views.register, {'template_name': 'accounts/register.html'}, name='accounts_register'),
    url(r'^register/complete/$', views.register_complete, {'template_name': 'account/register_complete.html'},name='accounts_register_complete'),
    url(r'^login/$', views.mllogin, {'template_name': 'accounts/login.html'}, name='accounts_login'),
    url(r'^profile/$', views.mllogin_profile, {'template_name': 'accounts/user_profile.html'},name='accounts_profile'),
    url(r'^logout/$', views.mllogout, {'template_name': 'accounts/logout.html'}, name='accounts_logout'),
        
#    (r'accounts/register/$', 'register'),
#    (r'accounts/register/complete/$', 'regist_compete'),
#    (r'accounts/profile/$', 'index'),
)
#urlpatterns += patterns('magicsite.mgccms.views',
#    (r'^accounts/$', 'mllogin'),
#    (r'^accounts/login/$', 'mllogin'),
#    (r'^accounts/logout/$', 'mllogout'),
#)