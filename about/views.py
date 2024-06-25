from django.shortcuts import render
from django.views import generic
from .models import About, CollaborateRequest
from django.contrib import messages
from .forms import CollaborateForm

def about_me(request):
    """
    Renders the about page
    """
    about = About.objects.all().order_by('-updated_on').first()

    if request.method == "POST":
        print('Reveived POST request')
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Message sent successfully, I aim to respond in two working days.'
            )
    collaborate_form = CollaborateForm()
    
    return render ( # send variables to be accesssible in template
        request,
        "about/about.html",
        {"about": about,
        "collaborate_form": collaborate_form,
        }
    )
