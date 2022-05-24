import os
from celery import Celery
from celery.schedules import crontab

# стандартные настройки celery и  задач по расписнаию
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'google_sheet.settings')


app = Celery('google_sheet')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'update_data-every-single-minute': {
        'task': 'data.tasks.update_data',
        'schedule': crontab(),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}