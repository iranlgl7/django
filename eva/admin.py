from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Asignatura)
admin.site.register(Clase)
admin.site.register(ActividadEvaluativa)