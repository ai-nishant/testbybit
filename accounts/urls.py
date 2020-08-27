from django.urls import path
from .views import accounts_view , RegisterAPI , LoginAPI
from rest_framework.authtoken import views
urlpatterns = [
    path('token-auth', views.obtain_auth_token),
    path('register', RegisterAPI.as_view(), name='register'),
    path('login', LoginAPI.as_view(), name='login'),
    path('',accounts_view,name='accounts')
]