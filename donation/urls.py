from django.conf.urls import url
from django.contrib import admin
from . import views


app_name = 'donation'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = "index"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = "detail"),
    url(r'^login/$', views.UserCreate.as_view(), name="login"),
    #no signup url
]