from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
# Create your views here.

from django.contrib.auth import login,logout, authenticate
from . import forms
from .models import User

class UserSignUpView(View):
    """User SignUp View to register a user """

    template_name  =  'User/register.html'

    def post(self, request):
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return render(request,self.template_name, {'form':form})
        
    def get(self, request):
        form = forms.RegistrationForm()
        return render(request,self.template_name, {'form':form})


class UserLoginView(View):
    """User Login View to login """

    template_name = "User/login.html"

    def get(self, request):
        form = forms.LoginForm()
        return render(request, self.template_name , {'form': form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)    
                return HttpResponseRedirect('/')
            else:
                return render(request, self.template_name , {'form': form})
        else:
            form = forms.LoginForm()
            return render(request, 'signup.html', {'form': form})
        

def user_logout(request):
    logout(request)
    return redirect('login')