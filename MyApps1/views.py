from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def display(request):
	ss = "<h1>Hello User, Welcome to Django First-Project(DJMyProject1) & First-App(MyApps1)</h1><hr />";
	return HttpResponse(ss);