"""Users URLs"""
# DJango
from django.urls import path
#Views
from users import views

urlpatterns = [
	#Management, eso va antes que los posts(ya que sin el login no se podrá acceder a los datos)
	path(route= 'login/',
		view =views.LoginView.as_view(),
		name ='login'
		),
	path(route = 'logout/',
		view = views.LogoutView.as_view(),
		name = 'logout'),

	path(route ='signup/',
		view = views.SignupView.as_view(),
		name ='signup'
		),
	path(route='me/profile/',
		view=views.UpdateProfileView.as_view(),
		name='update'
		),

]