from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import conference  # Correction ici : "Conference" avec majuscule, en supposant que le modèle commence par une majuscule
from Participant.models import*
from django.db.models import Count

class ReservationInLine(admin.StackedInline): #StackedInline est une classe fournie par Django admin qui permet d'afficher un modèle "en ligne"
    model=Reservation #réservation doit être liée au modèle Reservation
    extra=1 
    #En mettant extra=1, tu obtiens une ligne vide supplémentaire pour ajouter une nouvelle réservation. 
    # #Si tu voulais plus de lignes vides pour ajouter des réservations, tu pourrais augmenter ce nombre.
    readonly_fields=('reservation_date',)
    can_delete=True

class ConferenceDateFilter(admin.SimpleListFilter):
    title = "Date de la conférence" #Détermine le titre qui sera affiché dans l'interface d'administration pour ce filtre  # ba3d l BY 
    parameter_name = "conference_date"  #Définit le nom du paramètre qui sera utilisé dans l'URL lors du filtrage.

    def lookups(self, request, model_admin):
        return (
            ('past', 'Past Conferences'),
            ('upcoming', 'Upcoming Conferences'),
            ('today', 'Today Conferences'),
        )

    def queryset(self, request, queryset):
        today = timezone.now().date()
        if self.value() == 'past':  #Si l'utilisateur choisit "Past Conferences", le queryset est filtré
                                    #pour retourner toutes les conférences dont la date de fin (end_date) est antérieure à aujourd'hui.
            return queryset.filter(end_date__lt=today)
        elif self.value() == 'upcoming':
            return queryset.filter(start_date__gt=today)
        elif self.value() == 'today':
            return queryset.filter(start_date=today)
        return queryset
    
    
class ParticipantFilter(admin.SimpleListFilter): #La classe ParticipantFilter permet à l'administrateur de filtrer les conférences en fonction du nombre de participants 
    title="participant filter"
    parameter_name="participants"
    def lookups(self, request, model_admin) :
        return (
           ('0',('No participants')),
           ('more',('More participants'))
        )
    def queryset(self, request, queryset ):
        if self.value()=='0':
            return queryset.annotate(participant_count=Count('reservations')).filter(participant_count=0)
        if self.value() == '1':
            return queryset.annotate(participant_count=Count('reservations')).filter(participant_count__gt=0)
        return queryset
       
            
    
# Register your models here.
class ConferenceAdmin(admin.ModelAdmin):
    #affichage des conferences
    list_display = ('title', 'location', 'start_date', 'end_date', 'price') #Specifies which fields are shown in the list view of the admin interface ( wen search).
    search_fields = ('title',)  # recherche selon titre #Un filtre selon le titre de la conférence. 
    list_per_page = 2 #Limits the number of conferences shown per page to 2. #Activez la pagination sur le tableau de la liste des conférences. 
    ordering = ('start_date', 'title') #Orders the conferences by start date and title.
     # Ajout du filtre personnalisé ici
    list_filter = (ParticipantFilter,ConferenceDateFilter,)
    inlines = [ReservationInLine] #Afficher les entrées des réservations dans le formulaire d’ajout d’une conférence
    #fieldsets te permet de structurer les formulaires dans l'interface d'administration de manière plus lisible et intuitive. 
     
    fieldsets = (
        ('Description', {
            'fields': ('title', 'description', 'category', 'location','price','capacity')  # Correction des parenthèses
        }),
        ('Horaires', {
            'fields': ('start_date', 'end_date')  # Correction des parenthèses
        }),
        ('Documents', {
            'fields': ('program',)  # Correction des parenthèses
        })
    )
    
    readonly_fields=('created_at','update_at') #Ensures that the created_at and update_at fields are not editable.

admin.site.register(conference, ConferenceAdmin)  
