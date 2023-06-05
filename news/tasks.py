from celery import shared_task
import time

@shared_task
def new_news():
    time.sleep(10)
    print("Новости за последнюю неделю")
    return True
