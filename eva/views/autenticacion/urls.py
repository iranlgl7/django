from django.urls import path
from .views import Login, CustomLogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name='autenticacion/bienvenida.html'),name="bienvenida"),
    path('login/', Login.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('sesion/', TemplateView.as_view(template_name = 'autenticacion/sesion.html'), name='sesion'),
]
