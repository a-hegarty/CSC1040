from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomerForms
#from .models import *
#from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def userhome(request):
    return render(request, 'userhome.html')

def signup(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_invalid():
            form.save()
            return redirect('')

def order(request):
    return render(request, 'order.html')

def payment(request):
    return render(request, 'paymetn.html')

        
    