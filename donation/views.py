from .models import *
from django.views import generic
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

#no login view