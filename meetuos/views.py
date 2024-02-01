from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup
# Create your views here.
def index(request):
    meetups = Meetup.objects.all()
    return render(request,"meetuos/index.html",{
        "show_meetups":True,
        "meetups":meetups, 
    })

def home_page(request):
    return HttpResponse('Home Page')

def meetup_details(request,meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        return render(request,"meetuos/meetup-details.html",{
            "show_meetups":True,
            "meetup":selected_meetup
        })
    except Exception as ex:
        return render(request,"meetuos/meetup-details.html",{
            "show_meetups":False
        })