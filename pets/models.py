from django.db import models
from accounts.models import CustomUser
# Create your models here.
import os
import uuid


GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Others")
]


class PetOwner(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="pet_owner")
    name = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES, verbose_name='Gender*')
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name




def pet_photos_path(instance, filename):
    img_name, img_extension = os.path.splitext(filename)
    img_extension = img_extension.lower()
    filename = str(uuid.uuid4()) + img_extension
    path = os.path.join('pets/', filename)
    return path


class Blog(models.Model):
    title = models.CharField(max_length=500)
    short_description = models.CharField(max_length=2000)
    text = models.TextField()
    image = models.ImageField(upload_to=pet_photos_path, verbose_name='image*')
    date = models.DateField()


PetTypes = [
    ("cat", "Cat"),
    ("dog", "Dog"),
    ("birds", "Birds"),
    ("lab", "Lab animal"),
    ("O", "Other"),

]


class Pet(models.Model):
    owner = models.ForeignKey(PetOwner, on_delete=models.CASCADE, related_name="pets")
    name = models.CharField(max_length=100)
    animal_type = models.CharField(choices=PetTypes, max_length=25)
    color = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    seven_day_vaccinated = models.BooleanField(default=False)
    forty_five_day_vaccinated = models.BooleanField(default=False)
    yearly_vaccinated = models.BooleanField(default=False)

    profile_photo = models.ImageField(upload_to=pet_photos_path, )
    first_image = models.ImageField(upload_to=pet_photos_path, null=True, blank=True)
    second_image = models.ImageField(upload_to=pet_photos_path, null=True, blank=True)
    third_image = models.ImageField(upload_to=pet_photos_path, null=True, blank=True)
    forth_image = models.ImageField(upload_to=pet_photos_path, null=True, blank=True)
    fifth_image = models.ImageField(upload_to=pet_photos_path, null=True, blank=True)

    def __str__(self):
        return "{}, {}".format(self.name,  self.get_animal_type_display())


# class AppointmentRequest(models.Model):
#      pet = models.ForeignKey(Pet, related_name="appointment_requests", on_delete=models.CASCADE)
#      problem = models.TextField()
#      is_paid = models.BooleanField()



class SSLSetup(models.Model):
    store_id = models.CharField(max_length=100)
    store_password = models.CharField(max_length=100)
    base_url = models.CharField(max_length=1000)
    validation_api_url = models.CharField(max_length=1000)


SSL_STATUS_CHOICES = [
    ("PENDING", "PENDING"),
    ("PROCESSING", "PROCESSING"),
    ("COMPLETED", "COMPLETED"),
    ("VALID", "VALID"),
    ("FAILED", "FAILED"),
    ("CANCELLED", "CANCELLED"),
]


def forum_photos_path(instance, filename):
    img_name, img_extension = os.path.splitext(filename)
    img_extension = img_extension.lower()
    filename = str(uuid.uuid4()) + img_extension
    path = os.path.join('forums/', filename)
    return path

class ForumPost(models.Model):
    image = models.ImageField(upload_to=forum_photos_path, )
    title = models.CharField(max_length=500)
    details = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)


class ForumComment(models.Model):
    comment = models.CharField(max_length=10000)
    forum_post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)


#
# class SSLPaymentRecord(models.Model):
#     order_id = models.CharField(max_length=1000, unique=True)
#     initial_time = models.DateTimeField()
#     appointment_request = models.OneToOneField(AppointmentRequest, on_delete=models.CASCADE, related_name="ssl_record")
#     session_key = models.CharField(max_length=1000, null=True, blank=True)
#     transection_id = models.CharField(max_length=1000, null=True, blank=True)
#     val_id = models.CharField(max_length=1000, null=True, blank=True)
#     status = models.CharField(choices=SSL_STATUS_CHOICES, max_length=50, default="PENDING")
#     is_paid = models.BooleanField(default=False)
#     tran_date = models.CharField(max_length=100, null=True, blank=True)
#     amount = models.CharField(max_length=50, null=True, blank=True)
#     store_amount = models.CharField(max_length=50, null=True, blank=True)
#     card_type = models.CharField(max_length=50, null=True, blank=True)
#     card_no = models.CharField(max_length=500, null=True, blank=True)
#     currency = models.CharField(max_length=50, null=True, blank=True)
#     bank_tran_id = models.CharField(max_length=500, null=True, blank=True)
#     card_issuer = models.CharField(max_length=100, null=True, blank=True)
#     card_brand = models.CharField(max_length=100, null=True, blank=True)
#     card_issuer_country = models.CharField(max_length=100, null=True, blank=True)
#     card_issuer_country_code = models.CharField(max_length=100, null=True, blank=True)
#     currency_type = models.CharField(max_length=100, null=True, blank=True)
#     currency_amount = models.CharField(max_length=100, null=True, blank=True)
#     verify_sign = models.CharField(max_length=500, null=True, blank=True)
#     verify_key = models.CharField(max_length=2000, null=True, blank=True)
#     risk_level = models.CharField(max_length=100, null=True, blank=True)
#     risk_title = models.CharField(max_length=100, null=True, blank=True)

