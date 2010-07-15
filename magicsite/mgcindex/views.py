#!/usr/bin/env python
# -*- coding: GBK -*-
# Create your views here.
from django.conf import settings
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from models import mlRelease

def index(request,
          template_name="mgcindex/index.html"):

    #mldist_last = mlRelease.objects.latest()
    mldist_last = []
    mldist_all = mlRelease.objects.all()

    if mldist_all:
        mldist_last = mldist_all[0]

    return render_to_response(template_name,
        {'release': mldist_last, 'top': 5, 'navi_index': settings.SITE_CONFIG['navi_focous']},
        context_instance=RequestContext(request)
    )
    
    
from mgccms.views import mgccms_index, mgccms_article
def mgcindex_index(request, *args, **kwargs):
    ext = {}
    ext['navi_index'] = settings.SITE_CONFIG['navi_focous']
    return mgccms_index(request, 
        cmsModel = mlRelease, 
        ext_content = ext,
        template_name="mgcindex/list_all_release.html", 
        **kwargs)

def mgcindex_article(request, *args, **kwargs):
    ext = {}
    ext['navi_index'] = settings.SITE_CONFIG['navi_focous']
    return mgccms_article(request, 
        cmsModel = mlRelease, 
        ext_content = ext,
        template_name="mgcindex/article.html", 
        **kwargs)
