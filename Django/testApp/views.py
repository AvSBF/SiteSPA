import http
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