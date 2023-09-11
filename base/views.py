from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# rooms = [{'id':1,'name':'room1','capacity':10},
#          {'id':2,'name':'room2','capacity':20},
#          {'id':3,'name':'room3','capacity':30}
#          ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)
def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html',context)
# Create your views here.
