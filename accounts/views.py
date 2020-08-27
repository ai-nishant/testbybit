from django.shortcuts import render , HttpResponse
from rest_framework import serializers , generics
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view  , permission_classes
from .serializers import UserSerializer, RegisterSerializer
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login , authenticate , login

 

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
       
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        
        })


class LoginAPI(generics.GenericAPIView):  

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)








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