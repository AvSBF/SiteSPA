import http
from multiprocessing import context
import profile
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProfileModelForm

from testApp.forms import ProfileModelForm
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

def delete_profile(request, pk):
   profile = Profile.objects.get(id=pk)
   profile.delete()
   return redirect("/learn")

def create_profile(request):
   form = ProfileModelForm()
   if request.method == "POST":
      form = ProfileModelForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("/learn")
   context = {
      'form': form
   }
   return render(request, "create-profile.html", context)

def update_profile(request, pk):
   profile = Profile.objects.get(id=pk)
   form = ProfileModelForm()
   if request.method == "POST":
      form = ProfileModelForm(request.POST)
      if form.is_valid():
         firstName = form.cleaned_data['firstName']
         secondName = form.cleaned_data['secondName']
         nickname = form.cleaned_data['nickname']
         age = form.cleaned_data['age']
         profile.firstName = firstName
         profile.secondName = secondName
         profile.age = age
         profile.nickname  = nickname
         profile.save()
         return redirect("/learn")
   context = {
      'profile': profile,
      'form': form,
   }
   return render(request, "update-profile.html", context)
