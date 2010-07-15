try:
    from functools import update_wrapper, wraps
except ImportError:
    from django.utils.functional import update_wrapper, wraps  # Python 2.4 fallback.
    
from django.utils.decorators import available_attrs
from django.http import HttpResponseRedirect

def have_been_login(test_func, redirect_url=None):
    """
    Decorator for views that checks the test_func return value, 
    it will pass request.user parameter to test_func to help you to determine the result value.
    redirecting to the login_url page if the result value is false. 
    """
    if not redirect_url:
        from django.conf import settings
        redirect_url = settings.LOGIN_URL

    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not test_func(request.user):
                return view_func(request, *args, **kwargs)
            return HttpResponseRedirect(redirect_url)
        return wraps(view_func, assigned=available_attrs(view_func))(_wrapped_view)
    return decorator
