from django.urls import path
from .views import *

urlpatterns = [
    path('asignaturas/', ListarAsignaturas.as_view(), name='listar_asignaturas'),
    path('asignaturas/<int:asignatura_pk>/clases/', ListarClases.as_view(), name='listar_clases'),
    path('asignaturas/<int:asignatura_pk>/clases/<int:pk>/', VisualizarClase.as_view(), name='visualizar_clase'),
    path('asignaturas/<int:asignatura_pk>/actividades_evaluativas/', ListarActividadesEvaluativas.as_view(), name='listar_actividades_evaluativas'),
    path('asignaturas/<int:asignatura_pk>/actividades_evaluativas/<int:pk>/', VisualizarActividadEvaluativa.as_view(), name='visualizar_actividad_evaluativa'),
    path('asignaturas/<int:asignatura_pk>/actividades_evaluativas/responder/<int:pk>/', ResponderActividadEvaluativa.as_view(), name='responder_actividad_evaluativa'),
    path('asignaturas/<int:asignatura_pk>/profesores/', ListarProfesores.as_view(), name='listar_profesores'),
    path('asignaturas/<int:asignatura_pk>/profesores/<int:profesor_pk>/dudas/', ListarDudas.as_view(), name='listar_dudas'),
    path('asignaturas/<int:asignatura_pk>/profesores/<int:profesor_pk>/dudas/crear_duda/', CrearDuda.as_view(), name='crear_duda'),
    path('asignaturas/<int:asignatura_pk>/profesores/<int:profesor_pk>/dudas/modificar_duda/<int:pk>/', ModificarDuda.as_view(), name='modificar_duda'),
    path('asignaturas/<int:asignatura_pk>/profesores/<int:profesor_pk>/dudas/eliminar_duda/<int:pk>/', EliminarDuda.as_view(), name='eliminar_duda'),
    path('asignaturas/<int:asignatura_pk>/profesores/<int:profesor_pk>/dudas/visualizar_duda/<int:pk>/', VisualizarDuda.as_view(), name='visualizar_duda'),
]
