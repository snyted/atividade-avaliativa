from django.urls import path
from app import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('registrar_acao/', views.form_imprestimo, name="registrar"),
    path('cadastrar_equipamentos', views.cadastrar_equipamentos, name="cadastrar"),
    path('editar_equipamentos', views.listar_equipamentos, name='editar')
]