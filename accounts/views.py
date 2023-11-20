from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import SignupForm

# Create your views here.

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)

		if form.is_valid():
			user = form.save()
			authenticate(username=user.username, password=user.password)
			if user is not None:
				login(request, user)
				return redirect('/dashboard/')
	else:
		form = SignupForm()			
	return render(request, 'accounts/signup.html', {
		'form': form
		})
