from django.template import Library
from django.conf import settings

from mgcnews.models import mlNews
#from mgcguide.models import mlGuide
from mgcprojects.models import  mlProjects
from mgcindex.models import mlRelease
register = Library()

@register.inclusion_tag('mgcindex/snippet/index_news_list.html')
def index_news_list(top):
    news = mlNews.objects.all()[:top]
    return {'items': news}

#register.inclusion_tag('include/index_news_list.html')(index_news_list)

@register.inclusion_tag('mgcindex/snippet/index_guide_list.html')
def index_guide_list(top):
    news = mlGuide.objects.all()[:top]
    return {'items': news}

@register.inclusion_tag('mgcindex/snippet/index_project_list.html')
def index_projects_list(top):
    news = mlProjects.objects.all()[:top]
    return {'items': news}

# -----------------------------------------------------------
