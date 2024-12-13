
from django.urls import path
from .views import *

app_name = 'restaurant'
urlpatterns = [
    path("descriere", descriere_view, name="descriere_url"),
    path("meniu", meniu_view, name="meniu_url"),
    path('program', contact_view, name="contact_url"),
]
