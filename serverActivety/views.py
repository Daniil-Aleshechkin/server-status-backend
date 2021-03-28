from django.shortcuts import render
from datetime import datetime
from serverActivety.tasks import monitorTask
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import boto3
from mcstatus import MinecraftServer

from serverActivety.models import Time

# Create your views here.
@api_view(["GET"])
@permission_classes([AllowAny])
def celeryTest(request):
    monitorTask.delay()
    return Response(data={'result':1})

@api_view(["GET"])
@permission_classes([AllowAny])
def api_activety_detail_view(request):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance('i-0ce85af9e90203702')
    
    try:
        server = MinecraftServer.lookup(instance.public_ip_address)
        response = server.status().players.online
    except TypeError:
        response = None
    except ConnectionRefusedError:
        response = None

    activety = Time.objects.get(date=datetime.now().date())
    data = {}
    data['status'] = instance.state["Name"]
    data['ip'] = instance.public_ip_address
    data['time up'] = activety.uptime
    data['player count'] = response
    return Response(data=data)