#core library imports 
from django.shortcuts import render , HttpResponse ,get_list_or_404 , get_object_or_404
from django.http import JsonResponse

#Rest Framework Library imports
from rest_framework.views import APIView
from rest_framework.decorators import api_view  , permission_classes
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django_filters import rest_framework as filters
#Database model imports
from .models import Country , Player , Team , Match , Venue , Matchscorecard


#importing serializers below
from .serializers import CountrySerializer , VenueSerializer , PlayerSerializer , TeamSerializer ,MatchSerializer,MatchscorecardSerializer




@api_view(['GET'])
def api_index(request):
    api_end_points = {
        
        'Countries':'/countries',
        'teams':'/teams',
        'players':'/players',
        'player_info':'/player/<str:pk>/',
        'venue':'/venue',
        'matches':'/matches',
        'results':'/results',
        'tournament_score':'tournament_score'
    }
    return Response(api_end_points)




class CountriesViewset(viewsets.ModelViewSet):
    
   
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('cname',)



class VenueViewset(viewsets.ModelViewSet):    
    
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('venue_name',)


class TeamViewset(viewsets.ModelViewSet):    
    
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('team_name','country')

class PlayerViewset(viewsets.ModelViewSet):    
    
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('player_name','gender','age','playscore','country','team')

class MatchViewset(viewsets.ModelViewSet):    
    
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('')

class MatchscorecardViewset(viewsets.ModelViewSet):    
    
    queryset = Matchscorecard.objects.all()
    serializer_class = MatchscorecardSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('Matchscorecard_name',)

# class VenueViewset(viewsets.ModelViewSet):    
    
#     queryset = Venue.objects.all()
#     serializer_class = VenueSerializer
#     permission_classes = [IsAuthenticated]
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_fields = ('venue_name',)
