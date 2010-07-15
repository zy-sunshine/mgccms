# Create your views here.
from models import mlNews
from django.conf import settings
from mgccms.views import mgccms_index, mgccms_article

def mgcnews_index(request, *args, **kwargs):
    ext = {}
    ext['navi_news'] = settings.SITE_CONFIG['navi_focous']
    return mgccms_index(request, 
        cmsModel = mlNews, 
        ext_content = ext,
        template_name="mgcnews/index.html", 
        **kwargs)

def mgcnews_article(request, *args, **kwargs):
    ext = {}
    ext['navi_news'] = settings.SITE_CONFIG['navi_focous']
    return mgccms_article(request, 
        cmsModel = mlNews, 
        ext_content = ext,
        template_name="mgcnews/article.html", 
        **kwargs)
