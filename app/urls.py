from django.urls import path
from app import views
from .views import deletar_equipamento


urlpatterns = [
    path('', views.home, name="home"),
    path('registrar_acao/', views.form_imprestimo, name="registrar"),
    path('cadastrar_equipamentos', views.cadastrar_equipamentos, name="cadastrar"),
    path('editar_equipamentos', views.listar_equipamentos, name='editar'),
    path('deletar/<int:equipamento_id>/', deletar_equipamento, name='deletar_equipamento'),
    path('editar_equipamento/', views.editar_equipamento, name='editar_equipamento'),

]