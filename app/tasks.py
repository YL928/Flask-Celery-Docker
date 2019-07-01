from app import celery
import time
@celery.task(bind=True, track_started=True)
def long_task(self):
    time.sleep(10)
    return 10