from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed, JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from users.models import UserProfile

from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
import json

# Create your views here.

class Index(View):
	def get(self, request):
		if request.method == "GET":
			context = {}
			return render(request, 'users/index.html', context)
		else:
			return HttpResponseNotAllowed(['GET'])


class Register(View):
	def post(self, request):
		content = request.POST
		username = content.get('username')
		password = content.get('password')
		if not (username and password):
			return JsonResponse({'message': 'User does not exist'})

		user = User.objects.create_user(username=username, password=password)
		userprofile = UserProfile.objects.create(user=user)
		return  JsonResponse({'message': 'You are registered'})


class Login(View):
	def post(self, request):
		content = request.POST
		username = content.get('username')
		password = content.get('password')
		# print(request.user)
		if username and password:
			user = authenticate(username=username, password=password)
			if user:
				if user.is_active:
					login(request, user)
					return JsonResponse({
						'message': 'You are logged in!', 
						'user': request.user.username, 
						'logged_in': 'true',
					})
		return JsonResponse({'message': 'Invalid entry'})


class Logout(View):
	def post(self, request):
		logout(request)
		# print("hi")
		# return render(request, 'users/index.html')
		return HttpResponseRedirect('/users/index')


class RunSingleGame(View):
	def get(self, request):
		if request.method == "GET":
			# context = {}
			return render(request, 'users/_single_game_template.html')
			# return render(request, 'users/index.html', context)
		else:
			return HttpResponseNotAllowed(['GET'])


class SetTeams(View):
	def post(self, request):
		content = request.POST
		hometeam = content.get('hometeam')
		hometeamseason = content.get('hometeamseason')
		awayteam = content.get('awayteam')
		awayteamseason = content.get('awayteamseason')

		return render(request,'users/_set_teams_template.html', content)
		return  JsonResponse({'message': 'Teams are Set'})


# 	def get(self, request):
# 		if request.method == "GET":
# 			context = {}
# 			return render(request, 'users/_set_teams_template.html', context)
# 			# return render(request, 'users/_single_game_template.html', context)
# 			# return JsonResponse({'message': 'Teams are Set'})
# 		else:
# 			return HttpResponseNotAllowed(['GET'])
		

		# if request.method == "GET":
		# 	context = {}
		# 	return render(request, 'users/_set_teams_template.html', context)
		# else:
		# 	return HttpResponseNotAllowed(['GET'])

		# user = User.objects.create_user(username=username, password=password)
		# userprofile = UserProfile.objects.create(user=user)
		# return  JsonResponse({'message': 'You are registered'})




# class RunSeason(View):
# 	def get(self, request):
# 		if request.method == "GET":
# 			return render(request, 'users/_entire_season_template.html')			
# 		else:
# 			return HttpResponseNotAllowed(['GET'])






	# def get(self, request):
	# 	content = request.POST
	# 	# return HttpResponseRedirect('/users/index')
	# 	return JsonResponse({
	# 		'message': 'works',
	# 	})









