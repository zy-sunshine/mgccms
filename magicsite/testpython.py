import os
import sys
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
print ROOT_DIR
ext_apps = os.path.join(ROOT_DIR, 'apps'+os.path.sep+'external_apps')
mgc_apps = os.path.join(ROOT_DIR, 'apps'+os.path.sep+'mgcapps')
sys.path.append(ext_apps)
sys.path.append(mgc_apps)
import mgccms
import tinymce
