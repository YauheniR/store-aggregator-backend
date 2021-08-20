import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.task_routes = {
    "products.tasks.find_id_from_provider_product": {"queue": "products_tasks"},
    "categories.tasks.get_provider_category_count": {"queue": "categories_tasks"},
}

app.conf.beat_schedule = {
    "get_provider_category_every_day": {
        "task": "categories.tasks.get_provider_category_count",
        "schedule": crontab(minute=0, hour=0),
    }
}
