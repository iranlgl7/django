from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField 
from .models import *
from datetime import datetime

class LoginForm(AuthenticationForm):
  use_required_attribute = False
  username = UsernameField(widget=forms.TimeInput(attrs={'class':'form-control'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class DudaForm(forms.ModelForm):
  use_required_attribute = False
  class Meta:
    model = Duda
    fields = ['mensaje', 'sobre']
    widgets = {
      'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
      'sobre' : forms.TextInput(attrs={'class': 'form-control'}),
    }
    

class RespuestaDudaForm(forms.ModelForm):
  use_required_attribute = False
  class Meta:
    model = RespuestaDuda 
    fields = ['mensaje',]
    widgets = {
      'mensaje' : forms.Textarea(attrs={'class' : 'form-control'}),
    }
    

class ClaseForm(forms.ModelForm):
  use_required_attribute = False
  class Meta:
    model = Clase
    fields = ['numero', 'encabezado','cuerpo']
    widgets = {
      'numero': forms.TextInput(attrs={'class': 'form-control'}),
      'encabezado': forms.Textarea(attrs={'class': 'form-control', 'rows':'4'}),
      'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'rows':'2500'}),
    }
    

class ActividadEvaluativaForm(forms.ModelForm):
  use_required_attribute = False
  class Meta:
    model = ActividadEvaluativa 
    fields = ['numero', 'objetivoEvaluar', 'orden', 'estado']
    widgets = {
      'numero': forms.TextInput(attrs={'class': 'form-control'}),
      'objetivoEvaluar': forms.Textarea(attrs={'class': 'form-control', 'rows':'4'}),
      'orden': forms.Textarea(attrs={'class': 'form-control', 'rows':'2500'}),
      'estado': forms.Select(attrs={'class': 'form-select'}),
    }
    
    
class RespuestaActividadEvaluativaForm(forms.ModelForm):
  use_required_attribute = False
  class Meta:
    model = RespuestaActividadEvaluativa 
    fields = ['respuesta']
    widgets = {
      'respuesta': forms.Textarea(attrs={'class': 'form-control'}),
    }

    
