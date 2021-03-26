from django.shortcuts import render
from serverActivety.tasks import add
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


# Create your views here.
@api_view(["GET"])
@permission_classes([AllowAny])
def celeryTest(request):
    result = add.delay(4,7).get()
    print(result)
    return Response(data={'result':result})
