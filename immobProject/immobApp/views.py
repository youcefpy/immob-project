from django.shortcuts import render,redirect
from .forms import IntegrationForm
from django.http import FileResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from .models import Inscription

def inscription(request) :
    if request.method == "POST":
        form = IntegrationForm(request.POST)
        value_token = form.cleaned_data['id_inscription']
        data_inscription = Inscription.objects.filter()
        if form.is_valid():
        
            form.save()
            lines = []

            for data in data_inscription:
                lines.append( "nom : " + data.nom)
                lines.append(data.prenom)
                lines.append(data.email)
                lines.append(data.numero_tel)
                lines.append(data.ville)
                lines.append(data.id_inscription)
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
        

