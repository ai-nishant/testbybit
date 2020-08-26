from django.contrib import admin

from .models import Country , Player , Team , Match , Venue , Matchscorecard

admin.site.register(Country)
admin.site.register(Venue)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Matchscorecard)
