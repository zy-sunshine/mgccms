# Create your views here.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.models import User  
from django.shortcuts import render_to_response

from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

#@login_required
#@user_passes_test(user_login_status, login_url="/accounts/profile/")

from decorators import have_been_login

def register(request, template_name):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/accounts/register/complete/")
    else:
        form = UserCreationForm()
    return render_to_response(template_name, 
        {'form': form,},
        context_instance=RequestContext(request)
    )
def register_complete(request, template_name):
    return render_to_response(template_name,
        context_instance=RequestContext(request)
    )


def user_login_status(user):
    return user.is_authenticated()

@have_been_login(user_login_status, redirect_url="/accounts/profile/")
def mllogin(request, **kwargs):
    return login(request, **kwargs)

def mllogin_profile(request, template_name):
    return render_to_response(template_name,
        context_instance=RequestContext(request)
    )
    
def mllogout(request, **kwargs):
    return logout(request, **kwargs)


def about_pages(request, page):
    try:
        return direct_to_template(request, template="%s.html" % page)
    except TemplateDoesNotExist:
        raise Http404()
 
 