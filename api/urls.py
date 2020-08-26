from django.urls import path , include
from .views import ( api_index , CountriesViewset , VenueViewset,

TeamViewset,PlayerViewset , MatchViewset ,PlayerscoreViewset, MatchscorecardViewset )
from rest_framework.routers import SimpleRouter , DefaultRouter

routes = DefaultRouter()
routes.register('countries',CountriesViewset)
routes.register('venue',VenueViewset)
routes.register('team',TeamViewset)
routes.register('player',PlayerViewset)
routes.register('match',MatchViewset)
routes.register('playerscore',PlayerscoreViewset)
routes.register('matchscorecard',MatchscorecardViewset)

urlpatterns = [    
    path('',api_index,name='api_index'),
    path('',include(routes.urls)),
    # path('team',team_view,name='team_view'),
    # path('player',player_view,name='player_view'),
    # path('match',match_view,name='match_view'),
    # path('matchscorecard',matchscorecard_view,name='matchscorecard_view'),

]