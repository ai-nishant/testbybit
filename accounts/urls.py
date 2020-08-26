from django.urls import path
from .views import accounts_view 
from rest_framework.authtoken import views
urlpatterns = [
    path('token-auth', views.obtain_auth_token),
    path('',accounts_view,name='accounts')
]