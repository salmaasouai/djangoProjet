from django.db import models
from django.core.validators import RegexValidator
import re 
from django.core.exceptions import ValidationError
# Create your models here.
def validate_letters_only(value):
        if not re.match(r'^[A-Za-z\s]+$',value):
            raise ValueError('this field should only contain letters')
class category(models.Model):
    title=models.CharField(max_length=255,validators=[validate_letters_only])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class meta:
        verbose_name_plural="categories"
    def __str__(self):
        return f"title category = {self.title}" #Modifier le champs category du formulaire d’ajout d’une conférence en lui affectant une 
                                                #fonction d'autocomplétion, ce qui facilitera la sélection des catégories lors de la création ou 
                                                #de la modification d'une conférence.