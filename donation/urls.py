from django.conf.urls import url
from django.contrib import admin
from . import views


app_name = 'donation'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = "index"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = "detail"),
    url(r'^signup$', views.signup, name="signup"),
    # url(r'^login$',views.LoginView.as_view(), name="login"),
    url(r'^login$',views.signin, name="login"),
    #no login url
]