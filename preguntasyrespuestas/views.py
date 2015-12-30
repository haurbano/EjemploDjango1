from django.http import HttpResponse, Http404
from preguntasyrespuestas.models import Pregunta
from django.shortcuts import get_object_or_404, render_to_response

def index(request):
    preguntas = Pregunta.objects.all()
    return render_to_response('preguntasyrespuestas/index.html',
                                {'preguntas': preguntas})

def pregunta_detalle(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render_to_response('preguntasyrespuestas/pregunta_detalle.html',
                                {'pregunta':pregunta})
