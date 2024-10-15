from django.contrib import admin

from .models import Participant , Reservation
# Register your models here.


class ReservationAdmin(admin.ModelAdmin):
    #affichage des conferences
    list_display = ('conference', 'participant', 'confirmed', 'reservation_date') #Specifies which fields are shown in the list view of the admin interface ( wen search).
    def make_confirmed(self, request, queryset):
        queryset.update(confirmed=True)
    make_confirmed.short_description = "Marquer comme confirmé"

    # Action pour déconfirmer la réservation
    def make_unconfirmed(self, request, queryset):
        queryset.update(confirmed=False)
    make_unconfirmed.short_description = "Marquer comme non confirmé"

    # Définir les actions disponibles
    actions = [make_confirmed, make_unconfirmed]
class ParticipantAdmin(admin.ModelAdmin):
    #affichage des conferences
    list_display = ('cin', 'email', 'first_name', 'last_name', 'username','participant_category','get_reservation_count') #Specifies which fields are shown in the list view of the admin interface ( wen search).
    search_fields = ('cin','username',)  # recherche selon titre #Un filtre selon le titre de la conférence. 
    list_per_page = 2 #Limits the number of conferences shown per page to 2. #Activez la pagination sur le tableau de la liste des conférences. 
    ordering = ('participant_category',) #Orders the conferences by start date and title.
     # Ajout du filtre personnalisé ici
    
     
    #reservations est un ManyToManyField et ne peut pas être utilisé dans les fieldsets.
    fieldsets = (
        ('personal informations', {
            'fields': ('cin', 'email', 'first_name', 'last_name','username')  # Correction des parenthèses
        }),
        
        ('category', {
            'fields': ('participant_category',)  # Correction des parenthèses
        })
    )
    def get_reservation_count(self, obj):
        """Retourne le nombre de réservations pour le participant."""
        return obj.reservations.count()
    get_reservation_count.short_description = 'Number of Reservations' 
    
    readonly_fields=('created_at','updated_at')
     
admin.site.register(Reservation,ReservationAdmin) 

admin.site.register(Participant,ParticipantAdmin) 