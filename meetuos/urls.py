from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_page),
    path('meetuos/',views.index,name = "all-meetups"),
    path("meetuos/success",views.confirm_registration,name = "confirm-registration"),
    path('meetuos/<slug:meetup_slug>',views.meetup_details, name = "meetup-detail")
]