from django.urls import path
from . import views

urlpatterns = [
    # Início
    path('', views.home, name="home"),
    # Equipamentos
    path('cadastrar_equipamentos/', views.cadastrar_equipamentos, name="cadastrar"),
    path('editar_equipamentos/', views.editar_equipamentos, name='editar'),
    path('deletar/<int:equipamento_id>/', views.deletar_equipamento, name='deletar_equipamento'),
    path('editar_equipamento/<int:equipamento_id>/', views.editar_equipamento, name='editar_equipamento'),
    # Controle EPI
    path('registrar_acao/', views.registrar_acao, name="registrar"),
    path('relatorios_epi/', views.relatorios_epi, name='relatorio_epi'),
    # Colaborador
    path('cadastrar_colaborador/', views.cadastrar_colaborador, name='cadastrar_colaborador'),
    path('relatorios_colaborador/', views.relatorios_colaborador, name='relatorio_colaborador'),
    path('editar_colaborador/', views.editar_colaborador, name='editar_colaborador'),
]
