from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/post_detail', views.post_detail, name="post_detail"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

