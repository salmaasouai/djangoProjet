from django.shortcuts import render
from .models import Abonnements
from .formuser import abonnementForm
from django.views.generic import CreateView
from django.urls import reverse_lazy ,reverse
from django.contrib.auth.views import LoginView,LogoutView
import json
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from .models import Client
from gestionOffres.models import offre
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,redirect
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.exceptions import SuspiciousOperation
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

'''

class UserCreateView(CreateView):
    model=Client
    form_class =userForm
    template_name ="users/register.html"
    success_url = reverse_lazy('login')
'''
'''
User = get_user_model()
def abonner_offre(request, offre_id):
    try:
        # Récupérer l'ID utilisateur à partir des cookies
        user_id = request.COOKIES.get('user_id')
        
        # Vérifier si l'ID utilisateur existe dans les cookies
        if not user_id:
            return JsonResponse({'error': 'Utilisateur non identifié.'}, status=403)
        
        try:
            # Récupérer l'utilisateur à partir de l'ID des cookies
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Utilisateur introuvable.'}, status=404)
        
        # Vérifier si l'utilisateur est un client
        if not hasattr(user, 'is_client') or not user.is_client:
            return JsonResponse({'error': 'Seuls les clients peuvent souscrire à cette offre.'}, status=403)
        
        # Récupérer l'offre par ID
        selected_offre = get_object_or_404(offre, id=offre_id)
        
        # Vérifier que l'offre est toujours active (non expirée)
        if selected_offre.end_date < timezone.now().date():
            return JsonResponse({'error': 'Cette offre n\'est plus disponible.'}, status=400)
        
        # Vérifier qu'il n'y a pas déjà un abonnement pour le mois en cours
        start_of_month = timezone.now().replace(day=1)
        if Abonnements.objects.filter(participant=user, abonnement_date__gte=start_of_month).exists():
            return JsonResponse({'error': 'Vous avez déjà un abonnement ce mois-ci.'}, status=400)
        
        # Créer un nouvel abonnement
        abonnement = Abonnements.objects.create(
            offre=selected_offre,
            participant=user,
            confirmed=True,
            abonnement_date=timezone.now()
        )
        
        return JsonResponse({'message': 'Abonnement réussi!', 'abonnement_id': abonnement.id}, status=201)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
'''
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt  # Ce décorateur permet d'ignorer les restrictions CSRF pour les tests ou si vous gérez le CSRF via d'autres moyens.
def abonner_offre(request, offre_id, user_id):
    if request.method == 'POST':
        try:
            # Vérifier que l'utilisateur est authentifié et qu'il s'agit d'un client
            if not request.user.is_authenticated or not request.user.is_client:
                return JsonResponse({'error': 'Seuls les clients authentifiés peuvent s\'abonner.'}, status=403)

            # Récupérer l'instance de l'utilisateur et l'instance du client
            user = get_user_model().objects.get(pk=user_id)  # Récupérer l'utilisateur par ID
            client_instance = Client.objects.get(user=user)  # Lier l'utilisateur à son profil Client

            # Vérifier que l'utilisateur est bien un client
            if not client_instance.is_client:
                return JsonResponse({'error': 'Seuls les clients peuvent s\'abonner.'}, status=403)

            # Récupérer l'offre par ID
            selected_offre = get_object_or_404(offre, id=offre_id)

            # Vérifier que l'offre est toujours active (non expirée)
            if selected_offre.end_date < timezone.now().date():
                return JsonResponse({'error': 'Cette offre n\'est plus disponible.'}, status=400)

            # Vérifier qu'il n'y a pas déjà un abonnement pour le mois en cours
            start_of_month = timezone.now().replace(day=1)
            if Abonnements.objects.filter(participant=client_instance, abonnement_date__gte=start_of_month).exists():
                return JsonResponse({'error': 'Vous avez déjà un abonnement ce mois-ci.'}, status=400)

            # Créer un nouvel abonnement
            abonnement = Abonnements.objects.create(
                offre=selected_offre,
                participant=client_instance,
                confirmed=True,
                abonnement_date=timezone.now()
            )

            # Retourner une réponse JSON avec l'id de l'abonnement créé
            return JsonResponse({'message': 'Abonnement réussi!', 'abonnement_id': abonnement.id}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
def offre_list(request):
    offres = offre.objects.all()  # Récupérer les offres
    

    # Vérifier si l'utilisateur est un client connecté
    client_instance = Client.objects.get(user=request.user)

    return render(request, 'listOffre.html', {
        'offres': offres,
        'client_instance': client_instance,
    })
    
    
class LoginCustomView(LoginView):
    template_name='users/login.html'
    def get_success_url(self):
        return reverse('listViewoffre')