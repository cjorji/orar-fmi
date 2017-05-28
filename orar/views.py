from django.shortcuts import render

# Create your views here.
from .models import Elev
from .models import Event
from .models import Profesor
from .models import Room



def view_my_events(request):
    current_user = request.user
    elev = Elev.objects.get(user=current_user)
    events = Event.objects.filter(elev=elev)
    return render(request, 'my_events.html', {'events': events})


def all_group_events(request):
    current_user = request.user
    elev = Elev.objects.get(user=current_user)
    grupa = elev.grupa
    serie = elev.serie
    events = Event.objects.filter(grupa=grupa)
    # concateneaza cu Event.objects.filter(grupa=null,serie = elev.serie)
    events1 = Event.objects.filter(grupa=grupa, day=1)
    events1 = events1 | Event.objects.filter(grupa=None,serie=serie,day=1)
    events2 = Event.objects.filter(grupa=grupa, day=2)
    events2 = events2 | Event.objects.filter(grupa=None,serie=serie,day=2)
    events3 = Event.objects.filter(grupa=grupa, day=3)
    events3 = events3 | Event.objects.filter(grupa=None,serie=serie,day=3)

    events4 = Event.objects.filter(grupa=grupa, day=4)
    events4 = events4 | Event.objects.filter(grupa=None,serie=serie,day=4)

    events5 = Event.objects.filter(grupa=grupa, day=5)
    events4 = events5 | Event.objects.filter(grupa=None,serie=serie,day=5)

    teachers = Profesor.objects.all()
    rooms = Room.objects.all()

    return render(request, 'homepage.html', {'events': events, 'events1': events1,
                                             'events2': events2, 'events3': events3, 'events4': events4,
                                             'events5': events5, 'teachers': teachers, 'rooms':rooms})
