from django import forms
from datetime import date

class DisponibilitateForm(forms.Form):
    MESE_CATEGORII = [
        ("M1", "Masa 1"),
        ("M2", "Masa 2"),
    ]
    numar_masa = forms.ChoiceField(choices=MESE_CATEGORII, required=True)
    check_in = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': date.today()})
    )
    
    def clean_check_in(self):
        check_in = self.cleaned_data.get('check_in')

        if check_in.weekday() != 5:  #
            raise forms.ValidationError("Rezervările sunt disponibile doar pentru zilele de sâmbătă.")
        
        return check_in

    

