# Create your views here.
from django.conf import settings
from mgccms.views import mgccms_index, mgccms_article

from models import mlProjects

def mgcprojects_index(request, *args, **kwargs):
    ext = {}
    ext['navi_projects'] = settings.SITE_CONFIG['navi_focous']
    return mgccms_index(request, 
        cmsModel = mlProjects, 
        ext_content = ext,
        template_name="mgcprojects/index.html",
        **kwargs)

def mgcprojects_article(request, *args, **kwargs):
    ext = {}
    ext['navi_projects'] = settings.SITE_CONFIG['navi_focous']
    return mgccms_article(request, 
        cmsModel = mlProjects, 
        ext_content = ext,
        template_name="mgcprojects/article.html", 
        **kwargs)
    