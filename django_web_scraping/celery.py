from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab # scheduler

# default django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_web_scraping.settings')
app = Celery('django_web_scraping')
app.conf.timezone = 'UTC'
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# scheduled task execution
app.conf.beat_schedule = {
    # executes every 1 minute
    'scraping-task-one-min': {
        'task': 'news_scraping',
        'schedule': crontab()
    }
}