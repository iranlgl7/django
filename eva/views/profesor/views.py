from eva.models import *
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, View
from eva.forms import ClaseForm, ActividadEvaluativaForm, RespuestaDudaForm
from django.db import IntegrityError
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

class ListarClases(ListView):
  rol = 'profesor'
  model = Clase
  template_name = 'profesor/clases/listar_clases.html'
  
  def get_queryset(self):
      return Clase.objects.filter(asignatura = Profesor.objects.get(usuario = self.request.user).asignatura).order_by('numero')
  

class VisualizarClase(DetailView):
  rol = 'profesor'
  model = Clase
  template_name = 'profesor/clases/visualizar_clase.html'
  context_object_name = 'clase'
  
  
class CrearClase(CreateView):
  rol = 'profesor'
  model = Clase
  form_class = ClaseForm  
  template_name = 'profesor/clases/crear_clase.html'
  success_url = reverse_lazy('listar_clases_profesor')
  
  def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    ctx['crear'] = 1
    return ctx 
  
  def form_valid(self, form):
      try:
        form.instance.asignatura = self.request.user.usuario.profesor.asignatura
        return super().form_valid(form)
      except IntegrityError:
        form.add_error('numero', 'El número de clase seleccionado ya existe')
        return self.form_invalid(form)
      
      
class ModificarClase(UpdateView):
  rol = 'profesor'
  model = Clase
  form_class = ClaseForm  
  template_name = 'profesor/clases/crear_clase.html'
  success_url = reverse_lazy('listar_clases_profesor')
  
  def form_valid(self, form):
      try:
        return super().form_valid(form)
      except IntegrityError:
        form.add_error('numero', 'El número de clase seleccionado ya existe')
        return self.form_invalid(form)
      

class EliminarClase(DeleteView):
  rol = 'profesor'
  model = Clase
  template_name = 'layout/eliminar_elemento.html'
  success_url = reverse_lazy('listar_clases_profesor')
  
  def get_context_data(self, **kwargs):
    ctx= super().get_context_data(**kwargs)
    ctx['mensaje'] = '¿Seguro que desea eliminar la Clase?'
    ctx['dir'] = reverse('listar_clases_profesor')
    return ctx
    
        

class ListarActividadesEvaluativas(ListView):
  rol = 'profesor'
  model = ActividadEvaluativa
  template_name = 'profesor/actividades_evaluativas/listar_actividades_evaluativas.html'
  
  def get_queryset(self):
      return ActividadEvaluativa.objects.filter(asignatura = Profesor.objects.get(usuario = self.request.user).asignatura).order_by('numero')
    
 
class VisualizarActividadEvaluativa(DetailView):
  rol = 'profesor'
  model = ActividadEvaluativa
  template_name = 'profesor/actividades_evaluativas/visualizar_actividad_evaluativa.html'
  context_object_name = 'actividad'
 
 
class CrearActividadEvaluativa(CreateView):
  rol = 'profesor'
  model = ActividadEvaluativa
  form_class = ActividadEvaluativaForm  
  template_name = 'profesor/actividades_evaluativas/crear_actividad_evaluativa.html'
  success_url = reverse_lazy('listar_actividades_evaluativas_profesor')
  
  def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    ctx['crear'] = 1
    return ctx 
  
  def form_valid(self, form):
      try:
        form.instance.asignatura = self.request.user.usuario.profesor.asignatura
        actividad = form.save()
        for estudiante in Estudiante.objects.filter(grado = self.request.user.usuario.profesor.asignatura.grado):
          RespuestaActividadEvaluativa.objects.create(
            actividad = actividad,
            estudiante = estudiante,
          )
        return super().form_valid(form)
      except IntegrityError:
        form.add_error('numero', 'El número de actividad evaluativa seleccionado ya existe')
        return self.form_invalid(form)  
      
      
class ModificarActividadEvaluativa(UpdateView):
  rol = 'profesor'
  model = ActividadEvaluativa
  form_class = ActividadEvaluativaForm  
  template_name = 'profesor/actividades_evaluativas/crear_actividad_evaluativa.html'
  success_url = reverse_lazy('listar_actividades_evaluativas_profesor')
  
  def form_valid(self, form):
      try:
        return super().form_valid(form)
      except IntegrityError:
        form.add_error('numero', 'El número de actividad evaluativa seleccionado ya existe')
        print('wow')
        return self.form_invalid(form)  


class ModificarEstadoActividad(View):
  rol = 'profesor'
  def get(self, request, *args, **kwargs):
    actividad = ActividadEvaluativa.objects.get(pk = kwargs['pk'])
    actividad.estado = 'Habilitada' if actividad.estado == 'Deshabilitada' else 'Deshabilitada'
    actividad.save()
    return redirect('visualizar_actividad_evaluativa_profesor', pk = actividad.pk)
  
  
class EliminarActividadEvaluativa(DeleteView):
  rol = 'profesor'
  model = ActividadEvaluativa
  template_name = 'layout/eliminar_elemento.html'
  success_url = reverse_lazy('listar_actividades_evaluativas_profesor')
  
  def get_context_data(self, **kwargs):
    ctx= super().get_context_data(**kwargs)
    ctx['mensaje'] = '¿Seguro que desea eliminar la Actividad Evaluativa?'
    ctx['dir'] = reverse('listar_actividades_evaluativas_profesor')
    return ctx
  
  
class ListarEstudiantes(ListView):
  rol = 'profesor'
  model = Estudiante
  template_name = 'profesor/dudas/listar_estudiantes.html'
  
  def get_queryset(self):
     return Estudiante.objects.filter(
       grado = self.request.user.usuario.profesor.asignatura.grado
     ).order_by('usuario__first_name')
     
     
class ListarDudas(ListView):
  rol = 'profesor'
  model = Duda
  template_name = 'profesor/dudas/listar_dudas.html'
  
  def get_queryset(self):
     return Duda.objects.filter(
       profesor = self.request.user.usuario.profesor,
       estudiante = self.kwargs.get('estudiante_pk'),
     ).order_by('visto','-fecha')
     
  def get_context_data(self, **kwargs):
      ctx = super().get_context_data(**kwargs)
      ctx["estudiante"] =  Estudiante.objects.get(pk = self.kwargs.get('estudiante_pk'))
      return ctx
    
    
class VisualizarDuda(DetailView):
  rol = 'profesor'
  model = Duda
  template_name = 'profesor/dudas/visualizar_duda.html'
  context_object_name = 'duda'
  
  def get_context_data(self, **kwargs):
    duda = self.get_object()
    duda.visto = 1
    duda.save()
    ctx = super().get_context_data(**kwargs)
    return ctx
  
  
class CrearRespuestaDuda(CreateView):
  rol = 'profesor'
  model = RespuestaDuda
  template_name = 'profesor/dudas/crear_respuesta_duda.html'
  form_class = RespuestaDudaForm
  
  def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    ctx['duda'] = Duda.objects.get(pk = self.kwargs.get('duda_pk')).mensaje
    return ctx 
  
  def get_success_url(self):
     return reverse('visualizar_duda_profesor', kwargs={
       'estudiante_pk' : self.kwargs.get('estudiante_pk'),
       'pk' : self.kwargs.get('duda_pk')
     })
     
  def form_valid(self, form):
    duda = Duda.objects.get(pk = self.kwargs.get("duda_pk"))
    form.instance.duda = duda
    duda.resuelta = 1
    duda.save()
    return super().form_valid(form)