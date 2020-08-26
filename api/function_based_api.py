
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def countries_view(request):
#     if request.method == 'GET':
#         data = Country.objects.all()
#         dt = CountrySerializer(data, many=True)
        
#         return Response(dt.data,status=200)
#     return Response('change request type')





# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def venue_view(request):
#     if request.method == 'GET':
#         data = Venue.objects.all()
#         dt = VenueSerializer(data, many=True)
        
#         return Response(dt.data,status=200)
#     return Response('change request type')




# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def team_view(request):
#     if request.method == 'GET':
#         data = Team.objects.all()
#         dt = TeamSerializer(data, many=True)
        
#         return Response(dt.data,status=200)
#     return Response('change request type')



# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def player_view(request):
#     if request.method == 'GET':
#         data = Player.objects.all()
#         dt = PlayerSerializer(data, many=True)
        
#         return Response(dt.data,status=200)
#     return Response('change request type')



# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def match_view(request):
#     if request.method == 'GET':
#         data = Match.objects.all()
#         dt = MatchSerializer(data, many=True)
        
#         return Response(dt.data,status=200)
#     return Response('change request type')



# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def matchscorecard_view(request):
#     if request.method == 'GET':
#         data = Matchscorecard.objects.all()
#         dt = MatchscorecardSerializer(data, many=True)
        
#         return Response(dt.data,status=200)
#     return Response('change request type')