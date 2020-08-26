from django.shortcuts import render , HttpResponse
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view  , permission_classes


@api_view(['GET','POST'])
def accounts_view(request):
    if request.method == 'GET':
        data = {'verify': 'please fetch your token using username and password'}
        return Response(data=data,status=200)
    elif request.method == 'POST':        
        data = {'your token': 'your token'}
        return Response(data=data,status=200)
    else:
        return Response(data='change the GET METHOD to POST',status=404) 