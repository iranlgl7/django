from django.forms import BaseModelForm
from django.http import HttpResponse
from eva.models import *
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from eva.forms import RespuestaActividadEvaluativaForm, DudaForm
from django.urls import reverse, reverse_lazy


class ListarAsignaturas(ListView):
  rol = 'estudiante'
  model = Asignatura
  template_name = 'estudiante/asignaturas.html'
  
  def get_queryset(self):
    return Asignatura.objects.filter(grado = self.request.user.usuario.estudiante.grado)
  

class ListarClases(ListView):
  rol = 'estudiante'
  model = Clase
  template_name = 'estudiante/clases/listar_clases.html'
  
  def get_queryset(self):
      return Clase.objects.filter(asignatura__pk = self.kwargs.get('asignatura_pk')).order_by('numero')
    
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["asignatura"] =  Asignatura.objects.get(pk = self.kwargs.get('asignatura_pk'))
      return context
  
    
class VisualizarClase(DetailView):
  rol = 'estudiante'
  model = Clase
  template_name = 'estudiante/clases/visualizar_clase.html'
  context_object_name = 'clase'
  

class ListarActividadesEvaluativas(ListView):
  rol = 'estudiante'
  model = RespuestaActividadEvaluativa
  template_name = 'estudiante/actividades_evaluativas/listar_actividades_evaluativas.html'
  
  def get_queryset(self):
      return RespuestaActividadEvaluativa.objects.filter(
        actividad__asignatura__pk = self.kwargs.get('asignatura_pk'),
        estudiante = self.request.user.usuario.estudiante
        )
    
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["asignatura"] =  Asignatura.objects.get(pk = self.kwargs.get('asignatura_pk'))
      return context
  

class VisualizarActividadEvaluativa(DetailView):
  rol = 'estudiante'
  model = RespuestaActividadEvaluativa
  template_name = 'estudiante/actividades_evaluativas/visualizar_actividad_evaluativa.html'
  context_object_name = 'respuesta'
  
  
class ResponderActividadEvaluativa(UpdateView):
  rol = 'estudiante'
  model = RespuestaActividadEvaluativa
  template_name ='estudiante/actividades_evaluativas/crear_respuesta_actividad_evaluativa.html'
  form_class = RespuestaActividadEvaluativaForm
  
  def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    respuesta = RespuestaActividadEvaluativa.objects.get(pk = self.kwargs.get('pk'))
    respuesta.resuelta = 1
    respuesta.save()
    ctx['orden'] = respuesta.actividad.orden
    ctx['resuelta'] = respuesta.resuelta
    return ctx
  
  def get_success_url(self):
     return reverse('visualizar_actividad_evaluativa', kwargs={
       'asignatura_pk' : self.kwargs.get('asignatura_pk'),
       'pk' : self.kwargs.get('pk')
     })
  
    
class ListarProfesores(ListView):
  rol = 'estudiante'
  model = Profesor
  template_name = 'estudiante/dudas/listar_profesores.html'
  
  def get_queryset(self):
     return Profesor.objects.filter(
       asignatura__pk = self.kwargs.get('asignatura_pk')
     ).order_by('usuario__first_name')
     
  def get_context_data(self, **kwargs):
      ctx = super().get_context_data(**kwargs)
      ctx["asignatura"] =  Asignatura.objects.get(pk = self.kwargs.get('asignatura_pk'))
      return ctx
  
  
class ListarDudas(ListView):
  rol = 'estudiante'
  model = Duda
  template_name = 'estudiante/dudas/listar_dudas.html'
  
  def get_queryset(self):
     return Duda.objects.filter(
       estudiante = self.request.user.usuario.estudiante,
       profesor = self.kwargs.get('profesor_pk')
     ).order_by('-fecha')
     
  def get_context_data(self, **kwargs):
      ctx = super().get_context_data(**kwargs)
      ctx["asignatura"] =  Asignatura.objects.get(pk = self.kwargs.get('asignatura_pk'))
      ctx["profesor"] =  Profesor.objects.get(pk = self.kwargs.get('profesor_pk'))
      return ctx
    
    
class CrearDuda(CreateView):
  rol = 'estudiante'
  model = Duda
  template_name = 'estudiante/dudas/crear_duda.html'
  form_class = DudaForm
  
  def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    ctx['crear'] = 1
    return ctx 
  
  def get_success_url(self):
     return reverse('listar_dudas', kwargs={
       'asignatura_pk' : self.kwargs.get('asignatura_pk'),
       'profesor_pk' : self.kwargs.get('profesor_pk')
     })
     
  def form_valid(self, form):
    form.instance.estudiante = self.request.user.usuario.estudiante
    form.instance.profesor = Profesor.objects.get(pk = self.kwargs['profesor_pk'])
    return super().form_valid(form)
  

class ModificarDuda(UpdateView):
  rol = 'estudiante'
  model = Duda
  template_name = 'estudiante/dudas/crear_duda.html'
  form_class = DudaForm
  
  def get_success_url(self):
     return reverse('listar_dudas', kwargs={
       'asignatura_pk' : self.kwargs.get('asignatura_pk'),
       'profesor_pk' : self.kwargs.get('profesor_pk')
     })
     
     
class EliminarDuda(DeleteView):
  rol = 'estudiante'
  model = Duda
  template_name = 'layout/eliminar_elemento.html'
  
  def get_success_url(self):
     return reverse('listar_dudas', kwargs={
       'asignatura_pk' : self.kwargs.get('asignatura_pk'),
       'profesor_pk' : self.kwargs.get('profesor_pk')
     })
  
  def get_context_data(self, **kwargs):
    ctx= super().get_context_data(**kwargs)
    ctx['mensaje'] = '¿Seguro que desea eliminar la duda?'
    ctx['dir'] = reverse('listar_dudas', kwargs={
       'asignatura_pk' : self.kwargs.get('asignatura_pk'),
       'profesor_pk' : self.kwargs.get('profesor_pk')
     })
    return ctx
  
  
class VisualizarDuda(DetailView):
  rol = 'estudiante'
  model = Duda
  template_name = 'estudiante/dudas/visualizar_duda.html'
  context_object_name = 'duda'
  
  def get_context_data(self, **kwargs):
     ctx = super().get_context_data(**kwargs)
     try:
       respuesta = RespuestaDuda.objects.get(duda=self.get_object())
       ctx['respuesta'] = respuesta
       respuesta.visto = 1
       respuesta.save()
     except:
       pass 
     return ctx
  