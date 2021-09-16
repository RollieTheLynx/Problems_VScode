from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello world</h1>")
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        'my_text': 'This is about us',
        'my_number': 123,
        'my_list': [1,11,111],
        "conference_date": date(2025, 7, 14)
    }

    return render(request, "about.html", my_context)


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def socials_view(request, *args, **kwargs):
    return render(request, "socials.html", {})
