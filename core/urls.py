from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.getRoutes, name="API ROOT"),
    path('api/complementarios/', include('complementario.urls')),
    path('api/desarrollados/', include('desarrollado.urls')),
    path('api/enunciados/', include('enunciado.urls')),
    path('api/evaluaciones/', include('evaluacion.urls')),
    path('api/indirectas/', include('indirecta.urls')),
]
