from django.shortcuts import redirect
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render
           
class RequireLoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.path in settings.NONE_AUTH_ACCOUNT_PATHS and not request.user.is_authenticated and not request.path.startswith('/admin'):
            return redirect(settings.LOGIN_URL)
        

class RoleCheckMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path.startswith('/admin/') or request.path.startswith('/media/'):
            return
        if hasattr(view_func.view_class, 'rol'):
            if request.user.is_superuser:
                return redirect('/admin/')
            rol = getattr(view_func.view_class, 'rol')
            if request.user.usuario.rol != rol:
                ctx = {
                    'nombre': request.user.first_name,
                    'apellidos': request.user.last_name,
                    'rol_usuario': request.user.usuario.rol,
                    'rol': rol,
                }
                return render(request, 'autenticacion/acceso_restringido.html', ctx)
        return
           
