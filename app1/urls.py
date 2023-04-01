from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('sherbimet/',views.sherbimet, name='sherbimet'),
    path('personal/',views.personal, name='personal'),
    path('nutrion/',views.nutrion, name='nutrion'),
    path('online/',views.online, name='online'),
    path('blog/<slug:slug>',views.blog, name='blog'),
]
