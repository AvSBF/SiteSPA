import http
from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
   # return HttpResponse("My name is Anvar and I start actually remembering smth")
   return render(request, "AvSPortfolio.github.io/index.html")