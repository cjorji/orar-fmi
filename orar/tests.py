from django.test import TestCase
from .models import Room
from .models import User
# Create your tests here.
class AnimalTestCase(TestCase):
    def setUp(self):
        Room.objects.create(room_number=123)
        User.objects.create(username="yolo",password="woho")


    def test_room(self):
        room = Room.objects.get(room_number=123)


    def test_2(self):
        user = User.objects.get(username="yolo")

    def test_3(self):
        room = Room.objects.get(room_number=123)

    def test_4(self):
        room = Room.objects.get(room_number=123)
    def test_5(self):
        room = Room.objects.get(room_number=123)

