from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

class Home(TemplateView):

    template_name = 'index.html'
#    def get_success_url(self):
#    return reverse('home')
