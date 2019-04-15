'''Users views. '''
#DJango
#from django.contrib.auth import  authenticate, login, logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
#Models
from django.contrib.auth.models import User
from users.models import Profile

#Forms
from users.forms import SignupForm

class UserDetailView(LoginRequiredMixin, DetailView):
	'''User detail view.'''
	template_name = 'users/detail.html'
	slug_field = 'username'
	slug_url_kwarg = 'username'
	queryset = User.objects.all()
	context_object_name = 'user'

class SignupView(FormView):
	template_name ='users/signup.html'
	form_class = SignupForm
	success_url = reverse_lazy('users:login')

	def form_valid(self, form):
		'''Save form data.'''
		form.save()
		return super().form_valid(form)

class UpdateProfileView(LoginRequiredMixin, UpdateView):
	'''Update profile view.'''
	template_name = 'users/update_profile.html'
	model  = Profile
	fields = ['website','biography','phone_number','picture']
	def get_object(self):
		"""Return user's profile. """
		return self.request.user.profile

	def get_success_url(self):
		"""Return to user's profile. """
		username = self.object.user.username
		return reverse('users:detail',kwargs = {'username':username})

class LoginView(auth_views.LoginView):
	"""Login view."""
	template_name = 'users/login.html'

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
	"""Logout view."""
	template_name = 'users/logged_out.html'