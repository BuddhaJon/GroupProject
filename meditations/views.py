from .models import Meditation, Page_Visit, About, Profile, ForgotPassword
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'meditations/index.html')    #Might need context

class MeditationListView(generic.ListView):
    model = Meditation

class AboutView(generic.ListView):
    model = About

class ProfileView(LoginRequiredMixin, generic.ListView):
    model = Profile

class ForgotPasswordView(generic.ListView):
   model = ForgotPassword

# class MeditationHomeView(generic.ListView):
#     model = Meditation