from .models import *
from django import forms
from .forms import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

# Create your views here.
class IndexView(generic.ListView):
    context_object_name = 'Earthquakes'
    template_name = 'donation/UsQuakesindex.html'

    def get_queryset(self):
        return Earthquakes.objects.all()


class DetailView (generic.DetailView):
    model = Earthquakes
    template_name = ''


class UserCreate(CreateView):
    model = Customers
    fields = ['customer_name, customer_pw, customer_mail']

# class LoginView(View):
#     template_name = 'donation/login.html'
#
#     def post(self,request):
#         form = LoginForm(request.POST)
#         customer_mail = request.POST['customer_mail']
#         customer_pw = request.POST['customer_pw']
#         user = Customers.object.filter(customer_pw=customer_pw, customer_mail=customer_mail)
#
#         if user.exists():
#             return redirect('index')
#         else:
#             return HttpResponse('로그인 실패. 다시 시도해보세요')

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            # return render(request, 'donation/UsQuakesindex.html')
            return redirect('donation:index')

        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'donation/login.html', {'form': form})


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            # return render(request, 'donation/UsQuakesindex.html')
            return redirect('donation:index')
    else:
        form = UserForm()
        return render(request, 'donation/signup.html', {'form': form})