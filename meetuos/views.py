from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Meetup,Participant
from .form import RegistrationForm
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
        selected_meetup = Meetup.objects.get(slug = meetup_slug)
        if request.method == "GET":
            selected_meetup = Meetup.objects.get(slug=meetup_slug)
            registration_form = RegistrationForm()
        else:
            registration_form=RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                
                participant, _ = Participant.objects.get_or_create(email=user_email)
                participant = registration_form.save()
                selected_meetup.participent.add(participant)
                return redirect("confirm-registration")
                
        return render(request,"meetuos/meetup-details.html",{
                "show_meetups":True,
                "meetup":selected_meetup,
                "form":registration_form
            })
    except Exception as ex:
        print(ex)
        return render(request,"meetuos/meetup-details.html",{
            "show_meetups":True
        })
        
def confirm_registration(request):
    return render (request,"meetuos/registration-success.html")