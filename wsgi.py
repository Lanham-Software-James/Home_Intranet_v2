import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home_intranet_v2.settings')

application = get_wsgi_application()
