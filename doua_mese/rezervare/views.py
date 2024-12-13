from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView
from .models import Rezervare, Masa
from .forms import DisponibilitateForm


def verifica_disponibiltate(masa, check_in):
    rezervare_existenta = Rezervare.objects.filter(masa=masa, check_in=check_in).exists()
    return not rezervare_existenta

class RezervareView(LoginRequiredMixin, FormView):
    form_class = DisponibilitateForm
    template_name = "rezervare.html"
    login_url = '/accounts/login/' 

    def form_valid(self, form):
        
        data = form.cleaned_data
        mese_list = Masa.objects.filter(masa=data["numar_masa"])
        disponibilitate_mese = []

        for masa in mese_list:
            if verifica_disponibiltate(masa, data["check_in"]):
                disponibilitate_mese.append(masa)

        if disponibilitate_mese:
            masa = disponibilitate_mese[0]

            rezervare = Rezervare.objects.create(
                user=self.request.user,
                masa=masa,
                check_in=data["check_in"],
                price=masa.price  
            )
            rezervare.save()

            return render(self.request, 'rezervare_confirmare.html', {'rezervare': rezervare})
        else:
            return render(self.request, 'indisponibil.html')

class RezervariList(LoginRequiredMixin, ListView):
    model = Rezervare
    template_name = 'rezervari_list.html'
    context_object_name = 'rezervari'
    login_url = '/accounts/login/' 

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return Rezervare.objects.all()
        elif self.request.user.is_authenticated:
            return Rezervare.objects.filter(user=self.request.user)
        else:
            return Rezervare.objects.none() 
