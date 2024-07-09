from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from eva.models import Usuario
from eva.forms import LoginForm
from django.shortcuts import redirect
from django.contrib import messages

class Login(LoginView):
  redirect_authenticated_user = 1
  template_name = 'autenticacion/login.html'
  authentication_form = LoginForm
  success_url = 'login'
  
  def post(self, request, *args, **kwargs):
    usuario = request.POST['username']
    contrasenna = request.POST['password']
    user = authenticate(username = usuario, password = contrasenna)
    if user is not None:
      login(self.request, user)
      if user.is_superuser:
        return redirect('/admin/')
      if user.usuario.rol == 'estudiante':
        return redirect('listar_asignaturas')
      else:
        return redirect('listar_clases_profesor')
    else:
      messages.error(request, "El usuario insertado no existe.")
    return super().post(request, *args, **kwargs)


class CustomLogoutView(LogoutView):
    next_page = 'login'