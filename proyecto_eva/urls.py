from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('eva.views.autenticacion.urls') ),
    path('estudiante/',include('eva.views.estudiante.urls') ),
    path('profesor/',include('eva.views.profesor.urls') ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
