from django.http import HttpResponse
from django.shortcuts import render



#rooms
rooms = [
    {"id" : 1, "name" : "Let's learn Python"},
    {"id" : 2, "name" : "Django for Beginners"},
    {"id" : 3, "name" : "HTML & CSS"},
    {"id" : 4, "name" : "JavaScript"},
    {"id" : 5, "name" : "React for Beginners"},
    {"id" : 6, "name" : "All about VSC"},
    {"id" : 7, "name" : "GitHub"},
]

def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i

    context = {'room': room}
    return render(request, 'base/room.html',  context)
