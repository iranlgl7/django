from django.urls import path
from .views import *

urlpatterns = [
     path('clases/', ListarClases.as_view(), name='listar_clases_profesor'),
     path('clases/<int:pk>/', VisualizarClase.as_view(), name='visualizar_clase_profesor'),
     path('clases/crear_clase/', CrearClase.as_view(), name='crear_clase'),
     path('clases/modificar_clase/<int:pk>/', ModificarClase.as_view(), name='modificar_clase'),
     path('clases/eliminar_clase/<int:pk>/', EliminarClase.as_view(), name='eliminar_clase'),
     path('actividades_evaluativas/', ListarActividadesEvaluativas.as_view(), name='listar_actividades_evaluativas_profesor'),
     path('actividades_evaluativas/<int:pk>/', VisualizarActividadEvaluativa.as_view(), name='visualizar_actividad_evaluativa_profesor'),
     path('actividades_evaluativas/crear_actividad_evaluativa/', CrearActividadEvaluativa.as_view(), name='crear_actividad_evaluativa'),
     path('actividades_evaluativas/modificar_actividad_evaluativa/<int:pk>/', ModificarActividadEvaluativa.as_view(), name='modificar_actividad_evaluativa'),
     path('actividades_evaluativas/modificar_estado_actividad_evaluativa/<int:pk>/', ModificarEstadoActividad.as_view(), name='modificar_estado_actividad_evaluativa'),
     path('actividades_evaluativas/eliminar_actividad_evaluativa/<int:pk>/', EliminarActividadEvaluativa.as_view(), name='eliminar_actividad_evaluativa'),
     path('estudiantes/', ListarEstudiantes.as_view(), name='listar_estudiantes'),
     path('estudiantes/<int:estudiante_pk>/dudas/', ListarDudas.as_view(), name='listar_dudas_profesor'),
     path('estudiantes/<int:estudiante_pk>/dudas/<int:pk>/', VisualizarDuda.as_view(), name='visualizar_duda_profesor'),
     path('estudiantes/<int:estudiante_pk>/dudas/<int:duda_pk>/responder_duda/', CrearRespuestaDuda.as_view(), name='crear_respuesta_duda'),
]
