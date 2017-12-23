from .models import *
from django import forms
from django.http import HttpResponse
from django.views import generic, View
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, FormView


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

class LoginView(View):
    template_name = 'donation/login.html'

    def post(self,request):
        form = LoginForm(request.POST)
        customer_mail = request.POST['customer_mail']
        customer_pw = request.POST['customer_pw']
        user = Customers.object.filter(customer_pw=customer_pw, customer_mail=customer_mail)

        if user.exists():
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도해보세요')