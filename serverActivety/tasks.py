from celery import shared_task
from serverActivety.models import Time
from serverActivety.serializers import TimeSerializer

import boto3
from datetime import datetime

ec2 = boto3.resource('ec2')

@shared_task
def monitorTask():
    instance = ec2.Instance('i-00a959f48aaf55c53')

    try:
        time = Time.objects.get(date=datetime.now().date())
    except Time.DoesNotExist:
        time = Time.objects.create(date=datetime.now().date(),uptime=0,noPlayerTime=0)
    print(instance.state)
    if (instance.state['Name'] == 'running'):
        time.uptime += 1
    time.save()