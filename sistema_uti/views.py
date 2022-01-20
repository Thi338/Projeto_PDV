from django.shortcuts import render
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Create your views here.

def some_view(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "Hello world.")
    p.showPage()
    p.save()
    buffer.seek

