from rest_framework import serializers
from django.contrib.auth.models import User


user = User()


class UserRegistrationSerializer(serializers.Serializer):
    pass