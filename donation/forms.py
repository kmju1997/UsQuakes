from django import forms
from .models import Customers

class LoginForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['customer_mail', 'customer_pw']