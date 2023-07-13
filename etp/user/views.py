from django.shortcuts import render,redirect
from user.models import BookedTickets
from organizer.models import Eventdetails

def personalprofile(request):
    booked = BookedTickets.objects.all()
    return render(request,"uprofile.html", {'booked': booked})

def editprofile(request):
    return render(request,"editprofile.html")

def pep(request):
    dets=Eventdetails.objects.filter(eventName='FLUXUS').all()
    return render(request,"pep.html",{'dets':dets})

def cart(request):
    return render(request,"cart.html")



# Create your views here.
