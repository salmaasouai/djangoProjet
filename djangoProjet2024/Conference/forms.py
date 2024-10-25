from django import forms
from .models import conference

class ConferenceForm(forms.ModelForm):
    class Meta:
        model = conference
        fields = ['title', 'description', 'category', 'location', 'price', 'capacity', 'start_date', 'end_date', 'program']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),  # Personnalise le champ start_date
            'end_date': forms.DateInput(attrs={'type': 'date'}),    # Personnalise le champ end_date
        }