from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_page),
    path('meetuos/',views.index),
    path('details',views.meetup_details)
]