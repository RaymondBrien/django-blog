from django.shortcuts import render
from django.views import generic
from .models import About

def about_me(request):
    """
    Renders the about page
    """
    about = About.objects.all().order_by('-updated_on').first()
    
    return render(
        request,
        "about/about.html",
        {"about": about} # enables us to use 'about' variable in actual template, as it's defined here
    )