from django.db import models
from Categorie.models import category  # Import corrigé
from django.core.validators import MaxValueValidator, FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.
class conference(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    start_date = models.DateField(default=timezone.now)  # Utilisez timezone.now pour obtenir la date actuelle
    end_date=models.DateField()
    location=models.CharField(max_length=255)
    price=models.FloatField()
    capacity=models.IntegerField(validators=[MaxValueValidator(limit_value=900,message="capacity must be under 900")])
    program=models.FileField(upload_to='files/',validators=[FileExtensionValidator(allowed_extensions=['pdf','png','jpeg','jpg'])],error_messages="should contain certain types")
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE,related_name="Conference")  # 
#Chaque conférence doit être liée à une catégorie (ou type de conférence) via une 
#relation Many-to-One. Cela signifie qu'une catégorie peut regrouper plusieurs 
#conférences, mais chaque conférence ne peut appartenir qu'à une seule catégorie.
    def clean(self):
        if self.end_date <= self.start_date:
            raise ValidationError("End date must be after start date")
    class meta:
        constraints=[models.CheckConstraint(check=models.Q
            (
            start_date_gte=timezone.now().date()),
            name="the start date must be greater or equal than today "
            
                                            )
                     ]
       
    def __str__(self):
        return f"title conference = {self.title}"
            
    