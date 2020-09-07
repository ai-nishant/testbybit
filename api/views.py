#core library imports 
from django.shortcuts import render , HttpResponse ,get_list_or_404 , get_object_or_404
from django.http import JsonResponse
from django.db.models import Sum
#Rest Framework Library imports
from rest_framework.views import APIView
from rest_framework.decorators import api_view  , permission_classes
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django_filters import rest_framework as filters
#Database model imports
from .models import Country , Player , Team , Match , Venue , Matchscorecard , Playerscore


#importing serializers below
from .serializers import CountrySerializer , VenueSerializer , PlayerSerializer , TeamSerializer ,MatchSerializer,PlayerscoreSerializer,MatchscorecardSerializer



@api_view(['GET'])
def api_index(request):
    api_end_points = {
        
        'Countries':'/countries',
        'teams':'/team',
        'players':'/player',
        'player_info':'/player/<str:pk>/',
        'playerscorecard':'/playerscorecard/<str:pk>/',
        'venue':'/venue',
        'venue_info':'/venue/?id=',
        'match':'/match',
        'match_info':'/match/?id=',        
        'tournament_score':'tournament_score'
    }
    return Response(api_end_points)




class CountriesViewset(viewsets.ModelViewSet):
    
   
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('country_name',)



class VenueViewset(viewsets.ModelViewSet):    
    
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('venue_name',)

    def create(self,request,*args,**kwargs):
        venue_data = request.data 
        new_venue = Venue.objects.create(venue_name=venue_data['venue_name'],country= Country.objects.get(country_name=venue_data['country']))
        new_venue.save()
        serializer = VenueSerializer(new_venue)
        return Response(serializer.data)

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
    filterset_fields = ('player_name','gender','age','country','team')

    def create(self,request,*args,**kwargs):
        player_data = request.data 
        player_data = Player.objects.create(player_name=player_data['player_name'],
        age=player_data['age'],
        pic=player_data['pic'],
        gender=player_data['gender'],
        country= Country.objects.get(country_name=player_data['country']),
        team = Team.objects.get(team_name=player_data['team']))
        player_data.save()
        serializer = PlayerSerializer(player_data)
        return Response(serializer.data)

class MatchViewset(viewsets.ModelViewSet):    
    
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('')

    def create(self,request,*args,**kwargs):
        match_data = request.data 
        match_data = Match.objects.create(
        date=match_data['date'],
        match_no=match_data['match_no'],
        match_type=match_data['match_type'],
        start_time=match_data['start_time'],
        end_time=match_data['end_time'],
        team1 = Team.objects.get(team_name=match_data['team1']),
        team2 = Team.objects.get(team_name=match_data['team2']),
        venue= Venue.objects.get(venue_name=match_data['venue']),
        winner = Team.objects.get(team_name=match_data['winner']),
        looser = Team.objects.get(team_name=match_data['looser']),
        man_of_the_match = Player.objects.get(player_name=match_data['man_of_the_match']),
        bowler_of_the_match = Player.objects.get(player_name=match_data['bowler_of_the_match']),
        best_fielder = Player.objects.get(player_name=match_data['best_fielder']))
        match_data.save()
        serializer = MatchSerializer(match_data)
        return Response(serializer.data)

class PlayerscoreViewset(viewsets.ModelViewSet):    
    
    queryset = Playerscore.objects.all()
    serializer_class = PlayerscoreSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('match','player','team')


    def create(self,request,*args,**kwargs):
        playerscore_data = request.data 
        new_playerscore = Playerscore.objects.create(
            match = Match.objects.get(match_no=playerscore_data['match']),
            player = Player.objects.get(player_name=playerscore_data['player']),
            team = Team.objects.get(team_name=playerscore_data['team']),
            wide = playerscore_data['wide'],
            bounce = playerscore_data['bounce'],
            four = playerscore_data['four'],
            six  =    playerscore_data['six'])
        new_playerscore.save()
        serializer = PlayerscoreSerializer(new_playerscore)
        return Response(serializer.data)





class MatchscorecardViewset(viewsets.ModelViewSet):    
    
    queryset = Matchscorecard.objects.all()
    serializer_class = MatchscorecardSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('scores',)

