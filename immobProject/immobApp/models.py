from django.db import models
import uuid



class Inscription(models.Model):

    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(max_length = 254)
    numero_tel = models.CharField(max_length=10)
    ville = models.CharField(max_length=255)
    id_inscription = models.CharField(
        max_length=20,  
        unique=True,   
        editable=False,
        default='IMOBDZFR' + str(uuid.uuid4())[:8].upper()
    )
    

    def __str__(self):

        return f"{self.nom} {self.prenom} -- {self.id_inscription}"