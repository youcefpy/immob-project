from django.db import models
import uuid
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
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
    qr_code = models.ImageField(upload_to='qr_codes',blank=True)

    def __str__(self):

        return f"{self.nom} {self.prenom} -- {self.id_inscription}"
    
    def save(self,*args,**kwargs):
        qrcode_id_inscription = qrcode.make(self.id_inscription)
        canvas= Image.new("RGB",(290,290),'white') 
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_id_inscription)
        fname = f"id_inscr{self.id_inscription}.png"
        
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname,File(buffer),save=False)        
        canvas.close()
        super().save(*args,**kwargs)