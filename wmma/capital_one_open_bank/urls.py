from django.conf.urls import  include,url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home',),
    #url(r'^)
]
