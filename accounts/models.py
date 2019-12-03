from django.db import models
from django.contrib.auth.models import Group, AbstractUser
from django.core.validators import RegexValidator

ROLE_CHOICES = [
    ("doctor", "Doctor"),
    ("director", "Director"),
    ("pet_owner", "Pet Owner"),
    ('receptionist', "Receptionist"),
    ('inventory_manager', "Inventory Manager"),
    ('dev', "DEV"),
    ('accountant', "Accountant"),
    ('typist', "Typist"),
]


class CustomUser(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+8801XXXXXXXXX'. Up to 15 digits allowed.")
    contact_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)


    def __str__(self):
        return self.username



class CustomGroup(Group):
    class Meta:
        proxy = True
        app_label = 'accounts'
        verbose_name = 'Group'

