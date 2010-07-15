from django.template import Library
from django.conf import settings

from mgcprojects.models import mlProjects
register = Library()

@register.inclusion_tag("mgccms/snippet/top_digg.html")
def projects_top_digg():
    return {
            'news': mlProjects.objects.filter(status=2).select_related(depth=1).order_by("-digg")[:10],
            }
    
@register.inclusion_tag("mgccms/snippet/last_articles.html")
def projects_last_articles():
    news = mlProjects.objects.filter(status=2).select_related(depth=1).order_by("-publish")
    return {
            'news': news[:5]
    }
    
@register.inclusion_tag("mgccms/snippet/relate_tag_articles.html")
def projects_relate_tag_articles(num, news):
    tags = news.tags.split(',')
    relate_news = []
    for tag in tags:
        if tag:
            tag = get_object_or_404(Tag, name=tag)
            relate_news.extend(TaggedItem.objects.get_by_model(mlProjects, tag))
    return {
            'news': relate_news[:num]
            }
# TODO
# def relate_title_news():

@register.inclusion_tag("mgcprojects/snippet/projects_tag_list.html")
def projects_show_tags_for_article(obj):
    return {"obj": obj}

@register.inclusion_tag("mgcprojects/snippet/projects_month_links.html")
def projects_month_links():
    return {
            'dates': mlProjects.objects.dates('publish', 'month')[:12],
            }
    