from django.shortcuts import render

# Create your views here:


def index_view(request, *args, **kwargs):
    context = {}
    return render(request, "index.html", context)


def contacts_view(request, *args, **kwargs):
    context = {}
    return render(request, "contacts.html", context)


def about_view(request, *args, **kwargs):
    context = {}
    return render(request, "about.html", context)
