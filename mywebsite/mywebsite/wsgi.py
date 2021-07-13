"""
WSGI config for mywebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
import sys
import os

from django.core.wsgi import get_wsgi_application
path = 'C:/Users/99han/OneDrive/Belgeler/GitHub/djangoPortfolio'
if path not in sys.path:
	sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')

application = get_wsgi_application()
