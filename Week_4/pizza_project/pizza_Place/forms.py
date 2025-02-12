from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import *

#user signup
class CustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] # 2 passwords to verify passwords are the same

#user login / authectication
class CustomerLogin(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class OrderPizza(forms.ModelForm): 
    class Meta:
        model = Pizza
        fields = ['size', 'crust', 'gluten', 'sauce', 'cheese', 'toppings', 'additional_notes']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment_Details
        fields = ['name', 'address', 'card_number', 'card_expiry', 'cvv']

