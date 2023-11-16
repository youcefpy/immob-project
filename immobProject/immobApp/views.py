from django.shortcuts import render,redirect
from .forms import IntegrationForm
from django.http import FileResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from .models import Inscription
from immobProject.renderers import render_to_pdf
def inscription(request) :
    if request.method == "POST":
        form = IntegrationForm(request.POST)
        if form.is_valid():
            form.save()
            data_inscription = Inscription.objects.last()            
            lines = []
   
            lines.append("nom : " + data_inscription.nom)
            lines.append("prenom :=> "+data_inscription.prenom)
            lines.append("email =>" + data_inscription.email)
            lines.append("Numero tel => " +data_inscription.numero_tel)
            lines.append("Ville =>" +data_inscription.ville)
            lines.append("Id_Inscription =>"+data_inscription.id_inscription)
            lines.append("=========================================")


            buffer = BytesIO()
            pdf_object = canvas.Canvas(buffer,pagesize=letter,bottomup=0)
            txt_object = pdf_object.beginText()
            txt_object.setTextOrigin(inch,inch)
            for line in lines : 
                txt_object.textLine(line)
            pdf_object.drawText(txt_object)
            pdf_object.showPage()
            pdf_object.save()
            buffer.seek(0)

            
            return FileResponse(buffer,as_attachment=True,filename="test.pdf")
        
    else : 
        form = IntegrationForm()

    context = {
        'form' : form
    }
    return render(request,'inscription.html',context)
        

def pdf_view(request,*args,**kwargs):
    data_inscription = Inscription.objects.last()
    data = {
    
        "nom" : data_inscription.nom,
        "prenom":data_inscription.prenom,
        "ville": data_inscription.ville,
        "numero_tel":data_inscription.numero_tel,
        "id_inscriiption":data_inscription.id_inscription,

    }
    return render_to_pdf(request,"pdf_inscription.html",data)