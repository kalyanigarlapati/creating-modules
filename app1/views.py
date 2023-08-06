from django.shortcuts import render
from app1.models import *

# Create your views here.
def webpages(request):
    LWO=Webpage.objects.get(topic_name='parrot')
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    
    return render(request,'webpages.html',d)
    