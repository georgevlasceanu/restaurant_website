from django.urls import path
from .views import RezervareView, RezervariList

urlpatterns = [
    path('', RezervareView.as_view(), name="rezervare_url"),
    path('rezervari/', RezervariList.as_view(), name="rezervari_list_url"),
]