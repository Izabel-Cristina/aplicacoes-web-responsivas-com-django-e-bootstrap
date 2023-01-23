from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', views.get_bootstrap, name="bootstrap"),
   path("processa_formulario_v1",views.processa_formulario_v1, name="processa_formulario_v1"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)