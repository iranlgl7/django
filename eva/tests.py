from django.test import TestCase
from django.urls import reverse
from .models import Clase, Asignatura

class ClaseDetailView(TestCase):
    def setUp(self):
      self.clase = Clase.objects.create(
        asignatura = Asignatura.objects.create(
          nombre = 'Historia de Cuba'
        ),
        numero = 1,
        encabezado = 'La Sublevación de los vegueros',
        cuerpo = 'Cuerpo de Prueba',
      )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/profesor/clases/{self.clase.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('visualizar_clase_profesor', args=[self.clase.pk]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('visualizar_clase_profesor', args=[self.clase.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profesor/clases/visualizar_clase.html')
        