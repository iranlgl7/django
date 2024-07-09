from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.views.generic import View
from django.http import HttpResponse

class RoleRequiredMixin(View):
    role_required = None

    @method_decorator(require_http_methods(["GET"]))
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.usuario.rol == self.role_required:
            return HttpResponse('eRRORasasgasg')
        return super().dispatch(request, *args, **kwargs)