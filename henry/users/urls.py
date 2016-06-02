from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from users import views


urlpatterns = [
	url(r'^index$', views.Index.as_view(), name='index'),
	url(r'^register$', views.Register.as_view(), name='register'),
	url(r'^login$', views.Login.as_view(), name='login'),
	url(r'^logout$', views.Logout.as_view(), name='logout'),
	url(r'^singlegame$', views.RunSingleGame.as_view(), name='singlegame'),
	url(r'^setteams$', views.SetTeams.as_view(), name='setteams'),

	# url(r'^runseason$', views.RunSeason.as_view(), name='runseason'),

	
]