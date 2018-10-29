"""
WSGI config for pulifood project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/


import os
#from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pulifood.settings")

application = get_wsgi_application()
#application = Cling(get_wsgi_application())

"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pulifood.settings")
application = Cling(get_wsgi_application())
#application = get_wsgi_application()
