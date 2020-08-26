from rest_framework import serializers
from .models import Country , Player , Team , Match , Venue , Matchscorecard , Playerscore


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Country
        fields = ['id','country_name']


class VenueSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Venue
        fields = ['id','venue_name','country']
        depth = 1

    


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
        depth = 1


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        depth = 1


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
        depth = 1


class PlayerscoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playerscore
        fields = '__all__'
        depth = 1


class MatchscorecardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matchscorecard
        fields = '__all__'
        depth = 1