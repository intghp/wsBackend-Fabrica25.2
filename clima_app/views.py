from django.views import View
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

import os
import requests

from .models import Cidade, ConsultaTempo
from .forms import CidadeForm, ConsultaTempoForm

API_KEY = settings.OPENWEATHER_API_KEY
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

class ConsultaTempoView(View):
    def get(self, request):
        form = ConsultaTempoForm()
        cidades = Cidade.objects.all()
        return render(request, 'consultar_tempo.html', {'form': form, 'cidades': cidades})
    
    def post(self, request):
        form = ConsultaTempoForm(request.POST)
        if form.is_valid():
            cidade = form.cleaned_data['cidade']
            API_KEY = os.environ.get('OPENWEATHER_API_KEY')
            url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade.nome},{cidade.pais}&appid={API_KEY}&units=metric&lang=pt_br"
            
            try:
                response = requests.get(url)
                data = response.json()
                
                if response.status_code == 200:
                    consulta = ConsultaTempo(
                        cidade = cidade,
                        temperatura = data['main']['temp'],
                        descricao = data['weather'][0]['description'],
                        umidade = data['main']['humidity']
                    )
                    consulta.save()
                    
                    context = {
                        'cidade': cidade,
                        'temperatura': data['main']['temp'],
                        'descricao': data['weather'][0]['description'],
                        'umidade': data['main']['humidity'],
                        'vento': data['wind']['speed'],
                        'sucesso': True
                    }
                    return render(request, 'resultado_tempo.html', context)
                
                else:
                    messages.error(request, f'Erro ao consultar: {data.get('message')}')
                    
            except Exception as e:
                messages.error(request, f'Erro ao conectar com a API: {str(e)}')
        
        cidades = Cidade.objects.all()
        return render(request, 'consultar_tempo.html', {'form': form, 'cidades': cidades})

# def clima_teste(request):
#     cidade = "São Paulo"
#     pais = "BR"
#     api_key = 'CHAVE_API'
    
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade},{pais}&appid={api_key}&units=metric&lang=pt_br"
    
#     resposta = requests.get(url)
#     dados = resposta.json()
    
#     return JsonResponse(dados)