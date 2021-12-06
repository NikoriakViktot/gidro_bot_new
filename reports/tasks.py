from news.celery import app
from django.template.loader import render_to_string
import requests, os


@app.task
def add(x, y):
    return x + y


@app.task
def send_email(receiver, subject, template_name: str, vars: dict):
    from django.core.mail import send_mail
    text = render_to_string(template_name, vars)
    print(text)

    send_mail(
        subject,
        text,
        'from@example.com',
        [receiver],
        fail_silently=False, )


@app.task
def cron_task():
    print("Hello, world! I am CRON!")


@app.task
def notify_admin(notify):
    """
    curl -X POST \
     -H 'Content-Type: application/json' \
     -d '{"chat_id": "123456789", "text": "This is a test from curl", "disable_notification": true}' \
     https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage

    """

    requests.post(f"https://api.telegram.org/bot{os.getenv('TELEGRAM_API')}/sendMessage",
                  json={
                      "chat_id": os.getenv('CHAT_ID_LOVE'),
                      "text": notify,
                      "disable_notification": False})
