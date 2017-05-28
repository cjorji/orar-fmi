from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nume = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return str(self.nume)


class Serie(models.Model):
    numar_serie = models.IntegerField()

    def __unicode__(self):
        return str(self.numar_serie)


class Grupa(models.Model):
    numar = models.IntegerField()
    serie = models.ForeignKey(Serie,blank=True, null=True)

    def __unicode__(self):
        return str(self.numar)


class Room(models.Model):
    room_number = models.IntegerField()

    def __unicode__(self):
        return str(self.room_number)


class Event(models.Model):
    MY_CHOICES = (
        (1, 'Luni'),
        (2, 'Marti'),
        (3, 'Miercuri'),
        (4, 'Joi'),
        (5, 'Vineri'),
        (6, 'Sambata'),
        (7, 'Duminica'),
    )

    day = models.IntegerField(choices=MY_CHOICES, default=1)
    start_hour = models.CharField(default='8:00',max_length=5)
    end_hour = models.CharField(default='10:00',max_length=5)
    profesor = models.ForeignKey('Profesor', blank=True, null=True)
    title = models.CharField(max_length=200)
    grupa = models.ForeignKey(Grupa, blank=True, null=True)
    serie = models.ForeignKey(Serie,blank=True, null=True)
    sala = models.ForeignKey(Room, blank=True, null=True)

    def __unicode__(self):
        return self.title


class Elev(models.Model):
    events = models.ManyToManyField(Event, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grupa = models.ForeignKey(Grupa, blank=True, null=True)
    nume = models.CharField(max_length=100, blank=True, null=True)
    serie = models.ForeignKey(Serie, blank=True, null=True)

    def __unicode__(self):
        return self.nume + " " + str(self.grupa.numar)
