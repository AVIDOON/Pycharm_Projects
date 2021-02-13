from django.shortcuts import render
from django.http import  HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Starting Page')

def login(request):
    return HttpResponse('Login to your page')

def signup(request):
    return HttpResponse('Kindly Enter Your Details')

def welcome(request):
    return HttpResponse('Welcome to the Page')

def goToLogin(request):
    return HttpResponse('Now go to login page')