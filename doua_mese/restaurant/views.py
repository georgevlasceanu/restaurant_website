from django.shortcuts import render

# Create your views here.

def descriere_view(request):
    return render(request, "descriere.html")

def meniu_view(request):
    return render(request, "meniu.html")

def contact_view(request):
    return render(request, "contact.html")

