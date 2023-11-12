from django.contrib import admin
from .models import Inscription


class InscriptionAdmin(admin.ModelAdmin):
    list_display=('nom','prenom','email','numero_tel','ville','id_inscription')
    

admin.site.register(Inscription,InscriptionAdmin)