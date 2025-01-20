from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('escrever/', views.escrever, name='escrever'),
    path('cadastrar_pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('pessoa/excluir/<int:pessoa_id>/', views.excluir_pessoa, name='excluir_pessoa'),
    path('pessoas/', views.listar_pessoas, name='listar_pessoas'),
    path('dia/', views.dia, name='dia'),
    path('excluir_anotacao_dia/', views.excluir_anotacao_dia, name='excluir_anotacao_dia'),
    path('excluir_anotacao_individual/<int:id>/', views.excluir_anotacao_individual, name='excluir_anotacao_individual'),
    path('', views.home, name='home')
]