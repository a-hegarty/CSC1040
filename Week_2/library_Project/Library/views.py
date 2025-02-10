from django.http import HttpResponse
from django.shortcuts import render
import random

def index(request):
    return render(request, 'index.html')

def variable(request):
    a = 3
    b = 7
    x = 5
    # create a variable called x and give it a value
    # pass the variable x to the template variable.html with the name 'x'
    return render(request, 'variable.html', {'a': a, 'b': b, 'x': x })

def randomnumber(request):
   x = random.randint(0,100) # generate a random number between 0 and 100
   return render(request,'random.html',{'x':x})

def loop_example(request):
    names = ["John", "Paul", "George", "Ringo"]
    return render(request, 'loop_example.html', {'names':names})

def fizzbuzz(request):
    x = list(range(1, 101))#range starts at 1, ends before 101
    return render(request, 'fizzbuzz.html', {'x':x})