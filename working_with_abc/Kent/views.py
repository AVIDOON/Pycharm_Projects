from django.shortcuts import render
from django.http import  HttpResponse
from .models import Products
from .forms import NameForm


def homepage(request):
    products = Products.objects.all()
    return render(request, 'homepage.html', {'products': products})

def index(request):
    products = Products.objects.all()
    return render(request,'index.html',{'products':products})

def address(request):
    return render(request,'address.html')


def hello(request):
    return HttpResponse('Hello World')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def get_request(request):
    if request.method == 'Post':
        form = NameForm(request.Post)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print(name, email)

    form = NameForm()
    return render(request, 'form.html',{'form': form})


