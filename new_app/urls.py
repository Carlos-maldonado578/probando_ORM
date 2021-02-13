from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('usuarios', views.dev_usuarios),
    path('usuarios/delete/<int:id_usuario>', views.delete_usuario),
]