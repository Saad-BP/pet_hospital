from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hospital.models import *
# Create your views here.
from django.contrib import messages

def home(request):
    template = "common/home.html"

    context = {}

    return render(request, template, context)


def about(request):
    template = "common/home.html"

    context = {}

    return render(request, template, context)


def blogs(request):

    template = 'common/blogs.html'
    blogs = Blog.objects.filter(active=True).order_by('order')
    context = {
        'blogs': blogs,
    }

    if request.method == "POST":
        search = request.POST.get('search')
        blogs = Blog.objects.filter(title__icontains=search).order_by('order')

        context = {
            'blogs': blogs,
        }
        return render(request, template, context)


    return render(request, template, context)


def team(request):
    template = 'common/team_members.html'
    doctors = TeamMember.objects.filter(active=True).order_by('order')
    context = {
        'doctors': doctors,
    }

    return render(request, template, context)


def blog_details(request, id):
    template = "common/blog_details.html"
    blog = Blog.objects.get(id=id)
    context = {
        'blog': blog,
    }

    return render(request, template, context)
