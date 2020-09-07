from django.contrib import admin

from .models import Country , Player , Team , Match , Venue , Matchscorecard , Playerscore 

class PlayerScore(admin.ModelAdmin):
    model = Playerscore
    list_display = ('player','match','totalscore','team_total')



class TeamMatchScore(admin.ModelAdmin):
    model = Matchscorecard
    list_display = ('match','scores','team_match_score')

admin.site.register(Country)
admin.site.register(Venue)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Playerscore,PlayerScore)
admin.site.register(Matchscorecard,TeamMatchScore)
