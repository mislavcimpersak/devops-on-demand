"""
WSGI config for devops_on_demand project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops_on_demand.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "ProdConfig")

application = get_wsgi_application()
