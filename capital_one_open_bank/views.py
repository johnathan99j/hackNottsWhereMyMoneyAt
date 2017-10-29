from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse
import os


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
class Map_page(TemplateView):
    template_name = 'map.html'

class Home_page(TemplateView):

    template_name = 'index.html'
#    def get_success_url(self):
#    return reverse('home')


def submit(request):
    custId = request.POST['cf_id']
    os.system("geo.py " + custId)

    return render(request, 'map.html')
