from rest_framework import serializers
from .models import Country , Player , Team , Match , Venue , Matchscorecard , Playerscore


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Country
        fields = '__all__'


class VenueSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.country_name',read_only=True)
    class Meta:
        model = Venue
        fields = ['venue_name','country']

   

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


class PlayerscoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playerscore
        fields = '__all__'


class MatchscorecardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matchscorecard
        fields = '__all__'