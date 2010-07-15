# Create your views here.

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list
from django.conf import settings

from django.contrib import comments
from tagging.models import Tag, TaggedItem

from helper import archive_month_filter

def mgccms_index(request, cmsModel, ext_content,
        template_name,  
        username=None, tag=None, year=None, month=None):
    extra_context = {}
    if tag:
        tag = get_object_or_404(Tag, name=tag)
        extra_context['tag'] = tag
        posts = TaggedItem.objects.get_by_model(cmsModel, tag)
    else:
        posts = cmsModel.objects.all()
    posts = posts.filter(status=2).select_related(depth=1)
    if year and month:
        posts, t_context = archive_month_filter(year, month, posts, 'publish')
        extra_context.update(t_context)
    posts = posts.order_by("-publish")
    extra_context.update(ext_content)
    if username is not None:
        user = get_object_or_404(User, username=username)
        posts = posts.filter(author=user)
    return object_list(request,
                       posts,
                       paginate_by=5,
                       template_name=template_name,
                       extra_context=extra_context,
                       allow_empty=True)

def mgccms_article(request, cmsModel, ext_content, username, year, month, slug,
         template_name):
    post = cmsModel.objects.filter(slug=slug, publish__year=int(year), 
            publish__month=int(month)).filter(author__username=username)
    if not post:
        raise Http404
    if post[0].status == 1 and post[0].author != request.user:
        raise Http404
    post=post[0]

    user = request.user
    initial={}
    if user.is_authenticated():
        initial={'name': user.username, 'email': user.email}
    form = comments.get_form()(post, initial=initial)
    if request.method == "POST":
        data = request.POST.copy()
        form = comments.get_form()(post, data=data)
        if form.is_valid():
            comment = form.get_comment_object()
            comment.ip_address = request.META.get("REMOTE_ADDR", None)
            if request.user.is_authenticated():
                comment.user = request.user
            comment.save()

    if request.user.username != username:
        post.digg += 1
        post.save()
    content = {
        "news": post,
        "form": form,
    }
    content.update(ext_content)
    return render_to_response(
        template_name,
        content,
        context_instance=RequestContext(request))

