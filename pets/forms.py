from django import forms
from .models import *
from hospital.models import *
from accounts.models import CustomUser
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from bootstrap_datepicker_plus import DatePickerInput
import datetime

GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Others")
]


class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        exclude = ('owner', )

    def __init__(self, *args, **kwargs):
        super(PetForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        this_year = datetime.date.today().year

        self.fields['date_of_birth'].widget = forms.SelectDateWidget(
                                                        attrs={'class': 'form-control'}, years = range(this_year -20, this_year + 1))



class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('pet', 'service_type', 'details', 'phone', )

    def __init__(self, *args, **kwargs):
        pet_owner = kwargs.pop('pet_owner', True)
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['pet'].queryset = Pet.objects.filter(owner=pet_owner)



class ForumPostForm(forms.ModelForm):

    class Meta:
        model = ForumPost
        exclude = ('author', "date_time")


class ForumPostCommentForm(forms.ModelForm):


    class Meta:
        model = ForumComment
        exclude = ('author', "date_time", "forum_post")



