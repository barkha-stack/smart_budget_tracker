import os
from celery import Celery

# Tell Celery which Django settings to use
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

# Read CELERY settings from Django settings.py
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks.py from all installed apps
app.autodiscover_tasks()
