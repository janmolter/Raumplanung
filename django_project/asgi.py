import os

from django.core.wsgi import get_wsgi_application
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

application = get_default_application()
