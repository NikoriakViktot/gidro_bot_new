"""
Файл настроек Celery
https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
"""
from __future__ import absolute_import
import os
from gidro_bot.celery import Celery
from gidro_bot.celery import crontab

# этот код скопирован с manage.py
# он установит модуль настроек по умолчанию Django для приложения 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gidroBot.settings')

# здесь вы меняете имя
app = Celery("reports")

# Для получения настроек Django, связываем префикс "CELERY" с настройкой celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# загрузка tasks.py в приложение django
app.autodiscover_tasks()



app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-one-minute': {
        'task': 'front.tasks.cron_task',
        'schedule': crontab(),
    },
}



