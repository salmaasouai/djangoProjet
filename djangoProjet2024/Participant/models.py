from django.db import models
from django.contrib.auth.models import AbstractUser
from Conference.models import conference
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.
class Participant(AbstractUser):
    def email_validator(value):
        if not value.endswith('@esprit.tn'):
            raise ValidationError("EMAIL INVALID")
    cin_validator=RegexValidator(regex=r'^\d{8}$',message="his field should only contain 8 digits")
    cin=models.CharField(primary_key=True,max_length=8)
    email=models.EmailField(unique=True,max_length=255,validators=[email_validator])
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    username=models.CharField(max_length=255, unique=True)
    USERNAME_FIELD='username'
    CHOICES=(
        ('etudiant','etudiant'),
        ('chercheur','chercheur'),
        ('docteur','docteur'),
        ('enseignant','enseignant')
    )
    participant_category=models.CharField(max_length=255, choices=CHOICES)
    reservations=models.ManyToManyField(conference,through='Reservation',related_name='reservations')   # pour faire la relation avec conference :
    #un participant peut réserver plusieurs conférences, et qu'une conférence peut avoir plusieurs participants
    #Le mot-clé through spécifie un modèle intermédiaire qui gère la relation entre Participant et Conference
    #comment accéder à la relation depuis le modèle Conference
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class meta:
        verbose_name_plural="users" # pour changer le nom
        verbose_name="participant"


class Reservation(models.Model):
    conference=models.ForeignKey(conference, on_delete=models.CASCADE) # thez ml conferences l mwjoudin
    participant=models.ForeignKey(Participant, on_delete=models.CASCADE) # thez ml participants l mwjoudin
    confirmed=models.BooleanField(default=False)
    reservation_date=models.DateTimeField(auto_now_add=True)   
      
    def clean(self):
        if self.conference.start_date <= timezone.now().date():
            raise ValidationError("you can only reserve for upcoming conferences")  
        
       #pour compter le nombre de reservations fait par ce participant 
        reservation_count=Reservation.objects.filter(
            participant=self.participant,
            reservation_date=self.reservation_date
        ).count()
        
        
        if reservation_count >= 3:
            raise ValidationError("You can only have 3 reservations")
    class Meta:
        unique_together=('conference','participant')
        verbose_name_plural="Resevations"
    