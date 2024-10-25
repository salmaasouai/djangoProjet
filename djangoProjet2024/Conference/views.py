from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render #pour afficher un template en passant un dictionnaire
from .models import conference
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import ConferenceForm
from django.shortcuts import render, redirect
# Create your views here.

#Fonction pour afficher la liste des conférences 
def conferenceList(req):
    liste=conference.objects.all().order_by('-start_date')
    print(liste)
    return render(req,'conferences/conferencelist.html',
                  {'conferenceslist':liste})
 #Envoie les données à conferencelist.html, où elles seront accessibles sous le nom conferenceslist.

class ConferenceListView(ListView):
    model=conference
    template_name ='conferences/conference_liste.html'
    context_object_name='conferences' #permet d’accéder aux conférences sous le nom conferences dans le template.
    def get_queryset(self):
        return conference.objects.order_by('start_date')
    #urcharge la méthode pour trier les conférences par start_date en ordre croissant.
class DetailsViewConference(DetailView):
    model=conference
    template_name='conferences/conference_detail_view.html'
    context_object_name ='conference'
   
def conf_add(request):
    if request.method == 'POST':
        form = ConferenceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listeViewconf')
    else:
        form = ConferenceForm()

    return render(request, 'conferences/conference_form.html', {'form': form})

# Class-based view for adding a conference
class AddConference(CreateView):
    model = conference
    form_class = ConferenceForm
    template_name = 'conferences/conference_form.html'
    success_url = reverse_lazy('listeViewconf')

# Class-based view for updating a conference
class ConferenceUpdateView(UpdateView):
    
    model = conference
    form_class = ConferenceForm
    template_name = 'conferences/conference_form.html'
    success_url = reverse_lazy('listeViewconf') 
class ConferenceDeleteView(DeleteView):
    model = conference
    template_name = 'conferences/deleteCon.html'
    success_url = reverse_lazy('listeViewconf')