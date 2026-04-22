"""
WSGI config for career_advisor project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Career_Advisor_HOST.settings')

application = get_wsgi_application()
