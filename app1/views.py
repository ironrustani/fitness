
from django.shortcuts import render,get_object_or_404
from.models import Postimi
# Create your views here.

def home(request):
    return render(request, 'app1/home.html')
def about(request):
    return render(request, 'app1/about.html')
def contact(request):
    return render(request, 'app1/contact.html')
def sherbimet(request):
    sherbim = Postimi.objects.all
    return render(request, 'app1/programs.html',{'sherbimet':sherbim})
def postimet(request):
    return render(request, 'app1/postimet.html')
def personal(request):
    return render(request, 'app1/personal.html')
def nutrion(request):
    return render(request, 'app1/nutrion.html')
def online(request):
    return render(request, 'app1/online.html')
def blog(request,slug):
    item = get_object_or_404(Postimi,slug=slug)
    return render(request, 'app1/blog.html',{'blog':item})
