from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from hospital.models import *
from django.contrib import messages
# Create your views here.

@login_required(login_url='/accounts/sign_in')
def dashboard(request):
    template = "pets/owner_dashboard.html"
    pets = request.user.pet_owner.pets.all()
    context = {
        "pets": pets
    }

    return render(request, template, context)



@login_required(login_url='/accounts/sign_in')
def add_pet(request):
    template = "pets/add_pet.html"
    form = PetForm()

    if request.method == "POST":
        form = PetForm(request.POST, request.FILES or None)
        print(form.errors)
        if form.is_valid():
            pet = form.save(commit=False)
            if Pet.objects.filter(name=pet.name, owner=request.user.pet_owner).exists():
                messages.warning(request, "you already have a pet with the same name")
            else:
                pet.owner = request.user.pet_owner
                pet.save()
                return redirect("pets:dashboard")

    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required(login_url='/accounts/sign_in')
def add_forum(request):
    template = "pets/add_forum.html"
    form = ForumPostForm()

    if request.method == "POST":
        form = ForumPostForm(request.POST, request.FILES or None)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "your post has been submitted")
            return redirect("pets:forums")

    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required(login_url='/accounts/sign_in')
def forums(request):

    template = 'pets/forums.html'
    forums = ForumPost.objects.all().order_by('date_time')
    context = {
        'forums': forums,
    }


    return render(request, template, context)


@login_required(login_url='/accounts/sign_in')
def forum_details(request, id):
    template = "pets/forum-detail.html"
    forum = ForumPost.objects.get(id=id)
    form = ForumPostCommentForm()
    comments = forum.comments.all()
    context = {
        'forum': forum,
        'form': form,
        "comments": comments
    }



    if request.method == "POST":
        form = ForumPostCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.forum_post = forum
            comment.save()

            messages.success(request, "your comment has been added")
            return redirect("pets:forum_details", forum.id)

    return render(request, template, context)

@login_required(login_url='/accounts/sign_in')
def edit_pet(request, id):

    pet = Pet.objects.get(id=id)
    template = "pets/add_pet.html"
    form = PetForm(instance=pet)

    if request.method == "POST":
        form = PetForm(request.POST, request.FILES or None, instance=pet)
        if form.is_valid():
            pet = form.save(commit=False)
            if "name" in form.changed_data:
                if Pet.objects.filter(name=pet.name, owner=request.user.pet_owner).exists():
                    messages.warning(request, "you already have a pet with the same name")
                else:
                    pet.save()
                    return redirect("pets:dashboard")
            else:
                pet.save()
                return redirect("pets:dashboard")

    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required(login_url='/accounts/sign_in')
def pet_profile(request, id):

    pet = Pet.objects.get(id=id)
    owner = request.user.pet_owner

    if not owner.pets.filter(id=id).exists():
        messages.warning(request, "Not your pet")
        return redirect("pets:dashboard")


    template = "pets/pet_profile.html"

    context = {
        "pet": pet,
    }

    return render(request, template, context)


@login_required(login_url='/accounts/sign_in')
def appointmens(request):
    template = "pets/appointments.html"
    appointmens = Appointment.objects.filter(pet__owner=request.user.pet_owner).order_by('-attended', 'appointment_date', )

    context = {
        'appointments': appointmens
    }

    return render(request, template, context)


@login_required(login_url='/accounts/sign_in')
def new_appointment(request):
    template = "pets/new_appointment.html"
    owner = request.user.pet_owner

    form = AppointmentForm(pet_owner=owner)

    if request.method == "POST":
        form = AppointmentForm(request.POST, pet_owner=owner)
        form.save()
        messages.success(request, "Your appointment request has been submitted")
        return redirect("pets:appointments")

    context = {
        'form': form
    }

    return render(request, template, context)




@login_required(login_url='/accounts/sign_in')
def prescription(request, id):
    template = "pets/prescription.html"
    owner = request.user.pet_owner

    appointment = Appointment.objects.get(id=id)

    context = {
        'appointment': appointment
    }

    return render(request, template, context)




@login_required(login_url='/accounts/sign_in')
def products(request):
    template = "pets/products.html"

    products_list = Product.objects.filter(is_available=True).order_by('name')

    context = {
        'products': products_list
    }

    return render(request, template, context)

