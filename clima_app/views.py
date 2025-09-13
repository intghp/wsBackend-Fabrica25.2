from django.views import View
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Cidade
from .forms import CidadeForm
# Create your views here.
class HelloView(View):
    def get(self, request):
        return HttpResponse('Aplicação de Consulta do Tempo')
    
class CidadeListView(ListView):
    model = Cidade
    template_name = 'listar_cidades.html'
    context_object_name = 'cidades'

class CidadeCreateView(CreateView):
    model = Cidade
    form_class = CidadeForm
    template_name = 'criar_cidade.html'
    success_url = reverse_lazy('listar_cidades')
    
class CidadeUpdateView(UpdateView):
    model = Cidade
    form_class = CidadeForm
    template_name = 'criar_cidade.html'
    success_url = reverse_lazy('listar_cidades')
    
class CidadeDeleteView(DeleteView):
    model = Cidade
    template_name = 'deletar_cidade.html'
    context_object_name = 'cidade'
    success_url = reverse_lazy('listar_cidades')