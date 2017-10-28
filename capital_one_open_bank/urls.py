from django.conf.urls import  include,url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^map/$', views.Map_page.as_view(), name='map'),
    url(r'^$', views.Home_page.as_view(), name='home')
]
