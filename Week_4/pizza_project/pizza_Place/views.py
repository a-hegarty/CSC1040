from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def userhome(request, userid):
    user_id = get_object_or_404(User, id=userid)
    customer = OrderedPizza.objects.filter(customer=userid)
    past_orders = OrderedPizza.objects.filter(customer=userid)
    toppings = OrderedPizza.objects.filter(customer_id=userid)
    context = { 'userid':user_id,
                'history':past_orders,
                'toppings': toppings}
    return render(request, 'userhome.html', context=context)

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
    return redirect(request, 'logout.html')

def order(request, userid):
    user_id = get_object_or_404(User, id=userid)
    customer = get_object_or_404(User, id=userid)
    
    form = OrderPizza()
    
    if request.method == "POST":
        form = OrderPizza(request.POST)
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.customer = user_id
            pizza.save()
            form.save_m2m()
            id = OrderedPizza.objects.filter(customer_id=customer).values('id').last()['id']
            return redirect("payment", userid, id)
    context = {'orderpizza':form}
    context['userid'] = user_id
    return render(request, 'order.html', context=context)

def payment(request, userid, ordernum):
    user_id = get_object_or_404(User, id=userid)
    ordernumber = get_object_or_404(OrderedPizza, id=ordernum)
    form = PaymentForm()
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.order_id = ordernum
            payment.save()
            return redirect("vieworder", userid, ordernum)
    context = {'paymentform':form}
    context['userid'] = user_id
    context['ordernum'] = ordernumber
    return render(request, 'payment.html', context=context)

def vieworder(request, userid, ordernum):
    user_id = get_object_or_404(User, id=userid)
    ordernumber = get_object_or_404(OrderedPizza, id=ordernum)
    context = { 'userid':user_id, 
                'ordernum':ordernumber, 
                'ordered':ordernumber, 
                'toppings': ordernumber.toppings.all()}
    return render(request, 'vieworder.html', context=context)

        
    