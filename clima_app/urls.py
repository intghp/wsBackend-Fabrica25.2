from django.urls import path
from .views import (
    HelloView,
    CidadeListView,
    CidadeCreateView,
    CidadeUpdateView,
    CidadeDeleteView,
    ConsultaTempoView,
    #clima_teste
    )

urlpatterns = [
    path('', HelloView.as_view(), name='index'),
    path('cidades/', CidadeListView.as_view(), name='listar_cidades'),
    path('cidades/criar', CidadeCreateView.as_view(), name='criar_cidade'),
    path('cidades/editar/<int:pk>/', CidadeUpdateView.as_view(), name='atualizar_cidade'),
    path('cidades/deletar/<int:pk>/', CidadeDeleteView.as_view(), name='deletar_cidade'),
    path('tempo/consultar/', ConsultaTempoView.as_view(), name='consultar_tempo'),
    # path('clima_teste/', clima_teste),
]