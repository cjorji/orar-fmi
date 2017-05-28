from django.contrib import admin
from .models import Profesor
from .models import  Elev
from .models import Event
from .models import Grupa
from .models import Room
from .models import Serie
# Register your models here.

admin.site.register(Profesor)
admin.site.register(Elev)
admin.site.register(Event)
admin.site.register(Grupa)
admin.site.register(Room)
admin.site.register(Serie)