from django import forms
from .models import Customers
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    class Meta:
        # model = Customers
        # fields = ['customer_mail', 'customer_pw']
        model = User
        fields = ['username', 'password']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
