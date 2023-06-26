from .models import Meditation, Page_Visit, About
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, 'meditations/index.html')    #Might need context

class MeditationListView(generic.ListView):
    model = Meditation

class AboutView(generic.ListView):
     model = About


# class MeditationHomeView(generic.ListView):
#     model = Meditation