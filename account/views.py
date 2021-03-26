from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from rest_framework.authtoken.models import Token
from .serializers import AccountSerializer

@api_view(['POST',])
@permission_classes([AllowAny,])
# Create your views here.
def api_register_account_view(request):
    if request.method=="POST":
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data = {}
            data['email'] = account.email 
            data['username'] = account.username
            data['response'] = 
            data['token'] = Token.objects.get(user=account).key
            return Response(data=data,status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data=data,status=status.HTTP_400_BAD_REQUEST)

@api_view
@permission_classes([IsAuthenticated])
def api_detail_account_view(request):

    if request.method == "GET":
        account = request.user
        data = {}
        data['username'] = account.username
        data['email'] = account.email
        return Response(data=data)