from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    context = {"myName": "dinesh"}
    return render(request, "index.html", context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        messages.success(request, "Message Sent Successfully")
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def kulfi(request):
    return render(request, "kulfi.html")
