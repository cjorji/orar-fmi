from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.
from .models import Elev
from .models import Event
from .models import Profesor
from .models import Room


def view_my_events(request):

    current_user = request.user
    elev = Elev.objects.get(user=current_user)

    events = Event.objects.filter(elev=elev)
    # concateneaza cu Event.objects.filter(grupa=null,serie = elev.serie)
    events1 = Event.objects.filter(elev=elev, day=1).order_by('-start_hour')
    events2 = Event.objects.filter(elev=elev, day=2).order_by('-start_hour')
    events3 = Event.objects.filter(elev=elev, day=3).order_by('-start_hour')
    events4 = Event.objects.filter(elev=elev, day=4).order_by('-start_hour')
    events5 = Event.objects.filter(elev=elev, day=5).order_by('-start_hour')

    teachers = Profesor.objects.all()
    rooms = Room.objects.all()

    return render(request, 'my_events.html', {'events': events, 'events1': events1,
                                              'events2': events2, 'events3': events3, 'events4': events4,
                                              'events5': events5, 'teachers': teachers, 'rooms': rooms})


def add_event_to_user(request, event_id):
    current_user = request.user
    elev = Elev.objects.get(user=current_user)
    event = Event.objects.get(id=event_id)
    elev.events.add(event)
    return HttpResponseRedirect("/my_events/")


def remove_event_from_user(request, event_id):
    current_user = request.user
    elev = Elev.objects.get(user=current_user)
    event = Event.objects.get(id=event_id)
    elev.events.remove(event)
    return HttpResponseRedirect("/my_events/")


import datetime

def all_group_events(request):
    current_user = request.user
    currentDay = None
    from datetime import date
    week_num = date.today().day / 7
    if week_num % 2 == 0:
        ok = 1;
    else:
        ok = 2;

    if str(current_user) != "AnonymousUser":
        print(current_user)
        elev = Elev.objects.get(user=current_user)
        grupa = elev.grupa
        serie = elev.serie


        events = Event.objects.filter(grupa=grupa)

        # concateneaza cu Event.objects.filter(grupa=null,serie = elev.serie)
        events1 = Event.objects.filter(grupa=grupa, serie=None, day=1) | Event.objects.filter(grupa=None, serie=serie, day=1) | Event.objects.filter(grupa=None,
                                                                                                        serie=None,
                                                                                                        day=1)

        events1 = events1.filter(tip_saptamana=None) | events1.filter(tip_saptamana=ok)
        events1 = events1.order_by('-start_hour')

        events2 = Event.objects.filter(grupa=grupa, serie=None, day=2) | Event.objects.filter(grupa=None, serie=serie, day=2) | Event.objects.filter(grupa=None,
                                                                                                        serie=None,
                                                                                                        day=2)
        events2 = events2.filter(tip_saptamana=None) | events2.filter(tip_saptamana=ok)
        events2 = events2.order_by('-start_hour')

        events3 = Event.objects.filter(grupa=grupa, serie=None, day=3) | Event.objects.filter(grupa=None, serie=serie, day=3) | Event.objects.filter(grupa=None,
                                                                                                        serie=None,
                                                                                                        day=3)
        events3 = events3.filter(tip_saptamana=None) | events3.filter(tip_saptamana=ok)
        events3 = events3.order_by('-start_hour')

        events4 = Event.objects.filter(grupa=grupa, serie=None, day=4)
        events4 = events4 | Event.objects.filter(grupa=None, serie=serie, day=4) | Event.objects.filter(grupa=None,
                                                                                                        serie=None,
                                                                                                        day=4)
        events4 = events4.filter(tip_saptamana=None) | events4.filter(tip_saptamana=ok)
        events4 = events4.order_by('-start_hour')

        events5 = Event.objects.filter(grupa=grupa, serie=None, day=5)
        events5 = events5 | Event.objects.filter(grupa=None, serie=serie, day=5) | Event.objects.filter(grupa=None,
                                                                                                        serie=None,
                                                                                                        day=5)
        events5 = events5.order_by('-start_hour')

        day = datetime.datetime.today().weekday()
        print(datetime.datetime.today())
        print(day)
        day += 1
        if day < 6:
            switcher = {
                1: events1,
                2: events2,
                3: events3,
                4: events4,
                5: events5,
            }
            currentDay = switcher.get(day)

        print(day)

        teachers = Profesor.objects.all()
        rooms = Room.objects.all()
    else:
        events = None
        events1 = None
        events2 = None
        events3 = None
        events4 = None
        events5 = None
        teachers = None
        rooms = None
        currentDay = None

    return render(request, 'homepage.html', {'events': events, 'events1': events1,
                                             'events2': events2, 'events3': events3, 'events4': events4,
                                             'events5': events5, 'teachers': teachers, 'rooms': rooms, 'currentDay':currentDay,'weekType' : ok})


def parser(request):
    from bs4 import BeautifulSoup

    with open("343.html") as fp:
        soup = BeautifulSoup(fp, "html.parser")

    [s.extract() for s in soup('img')]

    table = soup.find_all('table')[0]  # Grab the first table
    rows = table.findAll('tr')

    i = 0
    response = ""
    response1 =""
    for tr in rows:
        cols = tr.findAll('td')

        # print(cols)
        for col in cols:
            if col:
                response += col.string + "<br></br>"
                response1 += col.string
                print(col.string)
    return HttpResponse(response1+ "<br></br>" + response)
