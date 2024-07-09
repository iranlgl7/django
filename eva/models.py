from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Usuario(models.Model):
  usuario = models.OneToOneField(User, on_delete = models.CASCADE)
  rol = models.CharField(max_length = 50)
  
  class Meta:
    verbose_name = 'Usuario'
    verbose_name_plural = 'Usuarios'
    db_table = 'usuario'
    
  def __str__(self):
    return f'{self.usuario.first_name} {self.usuario.last_name}'
  

class Estudiante(Usuario):
  grupo = models.CharField(max_length = 10, blank = 0, null = 0)
  grado = models.PositiveIntegerField(blank = 0, null = 0)
  
  class Meta: 
    verbose_name = 'Estudiante'
    verbose_name_plural = 'Estudiantes'
    db_table = 'estudiante'
  
  def save(self, *args, **kwargs):
    self.rol = 'estudiante'
    super().save(*args, **kwargs)
  

class Asignatura(models.Model):
  nombre = models.CharField(max_length = 255, blank = 0, null = 0)
  imagen = models.ImageField(upload_to='imagenes/asignaturas', null=1) 
  grado = grado = models.PositiveIntegerField(blank = 0, null = 0)
  
  class Meta:
    verbose_name = 'Asignatura'
    verbose_name_plural = 'Asignaturas'
    db_table = 'asignatura'
    
  def __str__(self):
    return self.nombre


class Profesor(Usuario):
  asignatura = models.ForeignKey(Asignatura, on_delete = models.DO_NOTHING, default = None, null = 1)
  
  class Meta: 
    verbose_name = 'Profesor'
    verbose_name_plural = 'Profesores'
    db_table = 'profesor'
    
  def save(self, *args, **kwargs):
    self.rol = 'profesor'
    super().save(*args, **kwargs)


class Duda(models.Model):
  estudiante = models.ForeignKey(Estudiante, null = 0, blank = 0, on_delete = models.CASCADE)
  profesor = models.ForeignKey(Profesor, null = 0, blank = 0, on_delete = models.CASCADE)
  sobre = models.CharField(max_length=255, blank=0, null=0)
  mensaje = models.TextField(null = 0, blank = 0)
  visto = models.BooleanField(default = False)
  fecha = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    verbose_name = 'Duda'
    verbose_name_plural = 'Dudas'
    db_table = 'duda'
  
  def __str__(self):
    return f'''
    estudiante: {self.estudiante.usuario.first_name} {self.estudiante.usuario.last_name}
    profesor: {self.profesor.usuario.first_name} {self.profesor.usuario.last_name}
    mensaje: {self.mensaje}
    fecha: {self.fecha} '''
    

class RespuestaDuda(models.Model):
  duda = models.OneToOneField(Duda, on_delete = models.CASCADE)
  mensaje = models.TextField(blank = 0, null = 0)
  visto = models.BooleanField(default = False)
  fecha = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    verbose_name = 'Respuesta_Duda'
    verbose_name_plural = 'Respuesta_Dudas'
    db_table = 'respuesta_duda'
    
  def __str__(self):
    return f'''
      datos de la duda:
      {self.duda.__str__()}
      datos de la respuesta:
      mensaje: {self.mensaje}
      estado: {self.estado}
      fecha: {self.fecha}
  '''


class Clase(models.Model):
  asignatura = models.ForeignKey(Asignatura, on_delete = models.CASCADE)
  numero = models.PositiveIntegerField(null = 0)
  encabezado = models.TextField(blank = 0, null = 0)
  cuerpo = models.TextField(null = 0, blank = 0)
  
  class Meta:
    verbose_name = 'Clase'
    verbose_name_plural = 'Clases'
    db_table = 'clase'
    unique_together = ['asignatura', 'numero']
    
  def __str__(self):
    return f'''
    asignatura: {self.asignatura.nombre}
    titulo: {self.encabezado}
    contenido: {self.cuerpo}
  '''


class ActividadEvaluativa(models.Model):
  estado_opciones = [
    ('Deshabilitada', 'Deshabilitada'),
    ('Habilitada', 'Habilitada'),
  ] 
  asignatura = models.ForeignKey(Asignatura, on_delete = models.CASCADE)
  numero = models.PositiveIntegerField(null = 0)
  objetivoEvaluar = models.TextField(null = 0, blank = 0)
  orden = models.TextField(blank = 0, null = 0)
  estado = models.CharField(max_length = 50, choices = estado_opciones, default = 'Deshabilitada')
  
  class Meta:
    verbose_name = 'ActividadEvaluativa'
    verbose_name_plural = 'ActividadesEvaluativas'
    db_table = 'actividad_evaluativa'
    unique_together = ['asignatura', 'numero']
    
  def __str__(self):
    return f'''
    asignatura: {self.asignatura.nombre}
    objetivo: {self.objetivoEvaluar}
    orden: {self.orden}
    fecha de cierre: {self.fecha_cierre}
  '''


class RespuestaActividadEvaluativa(models.Model):
  actividad = models.ForeignKey(ActividadEvaluativa, on_delete = models.CASCADE)
  estudiante = models.ForeignKey(Estudiante, on_delete = models.CASCADE)
  respuesta = models.TextField(blank = 1, null = 1)
  resuelta = models.BooleanField(default = 0)
  calificacion = models.FloatField(null = 1, blank = 1)
  
  class Meta:
    verbose_name = 'RespuestaActividadEvaluativa'
    verbose_name_plural = 'RespuestasActividadEvaluativa'
    db_table = 'respuesta_actividad_evaluativa'
    unique_together = ['actividad', 'estudiante']
  
  def __str__(self):
    return f'''
    estudiante: {self.estudiante.usuario.first_name}
    datos de la actividad: 
    {self.actividad.__str__()}
    respuesta: {self.respuesta}
    estado: {self.estado}
    calificacion: {self.calificacion if self.estado == 'revisado' else 'Sin Calificar'}
  '''
  
