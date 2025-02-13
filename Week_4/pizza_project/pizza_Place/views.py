from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from .forms import *
#from .models import *
#from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def userhome(request, userid):
    user_id = get_object_or_404(User, id=userid)
    return render(request, 'userhome.html', {'userid':user_id})

def signup(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {'registerform':form}
    return render(request, 'signup.html', context=context)

def login(request):
    form = CustomerLogin()
    if request.method == "POST":
        form = CustomerLogin(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:# if a user with the above id info exists at all
                auth.login(request, user)
                id = User.objects.filter(username=username).values('id')[0]['id']
                return redirect('userhome', id)
    context = {'loginform':form}
    return render(request, 'login.html', context=context)

def logout(request):
    auth.logout(request)
    return redirect('home')

def order(request, userid):

    form = OrderPizza()
    if request.method == "POST":
        form = OrderPizza(request.POST)
        if form.is_valid():
            form.save()
            return redirect("payment")
    context = {'orderpizza':form}
    return render(request, 'order.html', context=context)

def payment(request, order_number):
    order = get_object_or_404(id=order_number)
    form = PaymentForm()
    if request.method == "POST":
        form = PaymentForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("vieworder/")
    context = {'paymentform':form}
    return render(request, 'payment.html', context=context)

def vieworder(request, order_number):
    ordernum = get_object_or_404(id=order_number)
    return render(request, 'vieworder.html', {'ordernumber':ordernum})

        
    