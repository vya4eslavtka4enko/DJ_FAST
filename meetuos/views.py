from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    meetups = [
        { 
          "title":"A First Meetup",
          "location":"New York",
          "slug" : "a-firs-meetup"
        },
        {
         "title":"A Second Meetup",
         "location":"Paris",
         "slug": "a-second-meetup"
        }
    ]
    return render(request,"meetuos/index.html",{
        "show_meetups":True,
        "meetups":meetups, 
    })

def home_page(request):
    return HttpResponse('Home Page')

def meetup_details(request):
    selected_meetup = {
            "title":"A first meetup",
            "description":"This is the first meetup"
        }
    return render(request,"meetuos/meetup-details.html",{
        "meetup_title":selected_meetup["title"],
        "meetup_description":selected_meetup["description"]
    })