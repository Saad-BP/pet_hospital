from django import forms
from accounts.models import CustomUser
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from bootstrap_datepicker_plus import DatePickerInput


GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Others")
]


class SignUpForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    name = forms.CharField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    address = forms.CharField()
    phone = forms.CharField(max_length=11)
    date_of_birth = forms.DateField()

    class Meta:
        widgets = {
            'date_of_birth': DatePickerInput(
                options={
                    "format": "YYYY/MM/DD/",
                }
            ),
        }

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("password didn't match")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(username=email).exists():
            raise forms.ValidationError("user with this email already exists")

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 8:
            raise forms.ValidationError("Password must contain at least 8 characters")

        return password



    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'



class SignInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        email = self.cleaned_data.get("email").lower()
        password = self.cleaned_data.get("password").lower()

        if not CustomUser.objects.filter(username=email).exists():
            raise forms.ValidationError("user doesn't exist with this email")

        if CustomUser.objects.filter(username=email).first().role != "pet_owner":
            raise forms.ValidationError("You are not allowed to login")

        user = authenticate(username=email, password=password)

        if user is None:
            raise forms.ValidationError("Password did not match")

