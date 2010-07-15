#!/usr/bin/env python
# -*- coding: GBK -*-
from django.conf import settings

def common(request):
    """
    Adds media-related context variables to the context.

    """
    return {'SITE_CONFIG': settings.SITE_CONFIG}
