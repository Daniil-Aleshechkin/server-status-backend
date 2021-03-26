from celery import shared_task
from serverActivety.models import Time

@shared_task
def add(*args):
    sum = 0
    for x in range (10000000):
        for y in range (10000000):
           sum += x+y 
    return sum