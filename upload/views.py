from django.shortcuts import render
from . models import *
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'upload/home.html', {'posts':Post.objects.all()})


def about(request):
    return render(request, 'upload/about.html', {'title': 'About'})