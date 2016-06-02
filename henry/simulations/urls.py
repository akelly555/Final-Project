from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
# from users import views as users_views
from simulations import views 

urlpatterns = [

_single_game_template
	url(r'^create$', views.Create.as_view(), name='create'),
	url(r'^_single_game_template$', views.ViewYourPosts.as_view(), name='view-your-posts'),
	url(r'^view-your-page$', views.ViewYourPage.as_view(), name='view-your-page'),


]