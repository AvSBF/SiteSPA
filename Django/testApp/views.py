import http
from multiprocessing import context
import profile
from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile


def home_page(request):
   # return HttpResponse("My name is Anvar and I start actually remembering smth")
   return render(request, "index.html")

def learn(request):
   profiles = Profile.objects.all()
   context = {
      'profiles': profiles
   }
   return render(request, "learning_page.html", context)

def curr_profile(request, pk):
   profile = Profile.objects.get(id=pk)
   context = {
      'profile': profile,
   }
   return render(request, "detailed-profile.html", context=context )