import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'get-provider-category-every-day': {
        'task': 'categories.tasks.get_provider_category',
        'schedule': crontab(minute=0, hour=0,),
    }
}
