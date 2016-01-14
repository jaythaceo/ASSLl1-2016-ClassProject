from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegistrationForm, AccountUpdateForm
from models import UserAccounts

# Create your views here.
def index(request):
	return HttpResponse('This is the index.')

def newUser(request):
	form = RegistrationForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect('accounts:update')
	context = { 'form': form}
	return render(request, 'join.html', context)


def accountUpdate(request):
	#instance = get_object_or_404(UserAccounts, id = id )
	form =AccountUpdateForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect('accounts:profile')
	context = {
		#"user": instance,
		"form": form,
	}
	return render(request, 'update.html', context)


	#def accountUpdate(request, id=None):
	#instance = get_object_or_404(UserAccounts, id = id )
	#form =RegistrationForm(request.POST or None, request.FILES or None, 
	#	instance = instance)
	#if form.is_valid():
	#	instance = form.save(commit=False)
	#	instance.save()
	#	return redirect('accounts:profile', id = id)
	#context = {
	#	"user": instance,
	#	"form": form,
	#}
	#return render(request, 'update.html', context)