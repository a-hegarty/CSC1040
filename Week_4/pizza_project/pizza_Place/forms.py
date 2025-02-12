from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password_1', 'password_2'] # 2 passwords to verify passwords are the same

