#!/usr/bin/env python
import os
import sys
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
ext_apps = os.path.join(ROOT_DIR, 'apps'+os.path.sep+'external_apps')
mgc_apps = os.path.join(ROOT_DIR, 'apps'+os.path.sep+'mgcapps')
sys.path.append(ext_apps)
sys.path.append(mgc_apps)
from django.core.management import execute_manager
try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
