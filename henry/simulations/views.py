from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import View
# from users.models import UserProfile
# from django.http import Http404
import json


simulations

# Create your views here.

class ChooseHomeTeam(View):
	def get(self, request):
		content = request.POST
		team = content.get('team')
		season = content.get('season')
			team=team, 
			season=season, 
		team_list = [team.to_json() for team in teams]

		# teams = Team.objects.filter(team=team.team)

		return JsonResponse({
			'status': 'success', 
			'teams': teams_list, 
			'season': season,
		})	


class ChooseAwayTeam(View):	
	pass



# class ListAllTeams(View):
# 	def get(self, request):
# 		content = request.POST
# 		teams = Team.objects.filter(team=team.team)
# 		teams_list = [team.to_json() for team in teams]

# 		if len(teams_list) > 0:
# 			return JsonResponse({
# 				'status': 'success', 
# 				'teams': teams_list, 
# 			})	
# 		else:
# 			return JsonResponse({'error': 'something went terribly wrong here !'})







