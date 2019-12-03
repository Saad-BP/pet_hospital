from django.db import models
from accounts.models import *
from pets.models import *
# Create your models here.
import os
import uuid

EMPLOYEE_TYPES = [
    ("doctor", "Doctor"),
    ("director", "Director"),
    ('receptionist', "Receptionist"),
    ('inventory_manager', "Inventory Manager"),
    ('accountant', "Accountant"),
    ('typist', "Typist"),
]


def photos_path(instance, filename):
    img_name, img_extension = os.path.splitext(filename)
    img_extension = img_extension.lower()
    filename = str(uuid.uuid4()) + img_extension
    path = os.path.join('photos/', filename)
    return path

class Employee(models.Model):
    employee_id = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to=photos_path, verbose_name='Photo*', null=True)
    employee_type = models.CharField(choices=EMPLOYEE_TYPES, max_length=50)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    joining_date = models.DateField()

    def __str__(self):
        return str(self.employee_id)


def blog_photos_path(instance, filename):
    img_name, img_extension = os.path.splitext(filename)
    img_extension = img_extension.lower()
    filename = str(uuid.uuid4()) + img_extension
    path = os.path.join('blogs/', filename)
    return path


class Blog(models.Model):
    title = models.CharField(max_length=500)
    short_description = models.CharField(max_length=2000)
    text = models.TextField()
    image = models.ImageField(upload_to=blog_photos_path, verbose_name='image*')
    date = models.DateField()
    active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)


def team_photos_path(instance, filename):
    img_name, img_extension = os.path.splitext(filename)
    img_extension = img_extension.lower()
    filename = str(uuid.uuid4()) + img_extension
    path = os.path.join('team/', filename)
    return path


TEAM_MEMBER_DESIGNATION = [
    ('doctor', 'Doctor'),
    ('staff', 'Stuff'),
    ('assistant', 'Assistant'),
]


class TeamMember(models.Model):
    # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=team_photos_path)
    designation = models.CharField(max_length=50, choices=TEAM_MEMBER_DESIGNATION)
    details = models.TextField()
    phone = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="doctor")
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return "Dr. " +self.name

APPOINTMENT_TYPE = [
    ('grooming', "Grooming"),
    ('dentistry', "Dentistry"),
    ('boarding', "Boarding"),
    ('other', "Other"),
]

class Appointment(models.Model):
    pet = models.ForeignKey(Pet, related_name="appointments", on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50, choices=APPOINTMENT_TYPE)
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    appointment_date = models.DateField(null=True)
    details = models.TextField()
    phone = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    attended = models.BooleanField(default=False)
    payment_amount = models.FloatField(null=True)

class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    observation = models.TextField()
    treatment = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=1000)
    image = models.ImageField(upload_to=photos_path, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    url = models.CharField(max_length=5000)

    def __str__(self):
        return self.name



# class Receptionist(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     phone = models.CharField(max_length=100)
#
#
# class Accountant(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     phone = models.CharField(max_length=100)