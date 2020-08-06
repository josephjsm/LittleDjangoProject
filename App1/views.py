from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return render(request, "App1/index.html")

def greet(request, name):
	return render(request, "App1/greet.html", {
		"name": name.capitalize()
		})

def Jesoah(request):
	return HttpResponse("Hello, Jesoah")

def Mithr(request):
	return HttpResponse("Hello, Mithr")	