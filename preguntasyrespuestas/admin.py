from django.contrib import admin
from preguntasyrespuestas.models import Pregunta, Respuesta

class RespuestaInLine(admin.StackedInline):
	model = Respuesta
	extra = 3

class PreguntaAdmin(admin.ModelAdmin):
	inlines = [RespuestaInLine]
	list_display=('asunto', 'fecha_publicacion', 'publicado_hoy')
	list_filter = ['fecha_publicacion']

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta)

