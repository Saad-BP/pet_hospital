from django.shortcuts import render, redirect
from .form import SignInForm, SignUpForm
from .models import *
from pets.models import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def sign_in(request):
    template = "accounts/sign_in.html"

    form = SignInForm()

    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email").lower()
            user = CustomUser.objects.filter(username=email).first()
            if user.role == "pet_owner":
                password = form.cleaned_data.get("password").lower()
                user = authenticate(username=email, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect("pets:dashboard")

    context = {
        "form": form,
    }

    return render(request, template, context)

def sign_up(request):
    template = "accounts/sign_up.html"

    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('email').lower()
            password = form.cleaned_data.get('password').lower()
            user = CustomUser.objects.create_user(username=username,
                                                  password=password,
                                                  role='pet_owner')

            name = form.cleaned_data.get("name")
            gender = form.cleaned_data.get("gender")
            address = form.cleaned_data.get("address")
            phone = form.cleaned_data.get("phone")
            date_of_birth = form.cleaned_data.get("date_of_birth")

            pet_owner = PetOwner.objects.create(user=user, email=username, name=name, gender=gender, address=address, phone=phone, date_of_birth=date_of_birth)
            messages.success(request, "You have signed up successfully, please log in with your email and password")

            return redirect('accounts:sign_in')
            print(pet_owner)
        else:
            print(form.errors)

    context = {
        'form': form
    }


    return render(request, template, context)


def logout(request):
    auth_logout(request)
    # messages.success(request, "logged out")
    return redirect("common:home")