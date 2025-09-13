
# 📘 Projeto Fábrica de Software 2025.2

## 📌 Sobre o projeto

Este projeto consiste em um **sistema Django** para consulta de condições climáticas em tempo real, utilizando a **API OpenWeatherMap**

A aplicação foi desenvolvida com o seguintes critérios:

- **Entidade Cidade:** implementada com Class-Based-Views, permitindo o CRUD de cidades.
- **Entidade ConsultaTempo:** modelo que armazena os dados obtidos da API externa OpenWeatherMap e os expõe por meio de uma API própria.

Dessa forma, o sistema integra funcionalidades baseadas em templates **Django** com uma **API REST**.

## ⚙️ Tecnologias
- Python 3.12.0
- Django 5.2.6

## ✨ Funcionalidades
- ✅ Consulta em tempo real via **OpenWeatherApp API**
- ✅ Cadastro e Gerenciamento de Cidades
- ✅ Operações CRUD completas para a entidade **Cidade**







## 🚀 Como rodar o projeto

### 1. Clonar o repositório

```bash
  git clone https://github.com/intghp/wsBackend-Fabrica25.2
  cd wsBackend-Fabrica25.2
```

### 2. Criar e ativar ambiente virtual
```bash
  python -m venv venv
  venv/Scripts/activate
```

### 3. Instalar dependências
```bash
  pip install -r requirements.txt
```

### 4. Aplicar migrações
```bash
  python manage.py makemigrations
  python manage.py migrate
```

### 5. Rodar projeto
```bash
  python manage.py runserver
```
O projeto estará disponível em https://127.0.0.1:8000/


## API OpenWeatherMap

### EndPoint: Obter Clima Atual

```http
  GET data/2.5/weather?q={cidade.nome},{cidade.pais}&appid={API_KEY}&units=metric&lang=pt_br
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `cidade.nome` | `string` | **Obrigatório**. Nome da cidade |
| `cidade.pais` | `string` | **Opcional**. Código do país em duas letras. Recomendado para evitar ambiguidade|
| `appid` | `string` | **Obrigatório**. Chave de API do OpenWeatherMap|
| `units` | `string` | **Opcional**. Chave de API do OpenWeatherMap|
| `lang` | `string` | **Opcional**. Idioma da descrição do clima|

#### Exemplo de resposta JSON

```http
  {
  "coord": {
    "lon": -46.6361,
    "lat": -23.5475
  },
  "weather": [
    {
      "id": 803,
      "main": "Clouds",
      "description": "nublado",
      "icon": "04d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 18.89,
    "feels_like": 18.64,
    "temp_min": 18.58,
    "temp_max": 19.94,
    "pressure": 1022,
    "humidity": 69,
    "sea_level": 1022,
    "grnd_level": 930
  },
  "visibility": 10000,
  "wind": {
    "speed": 5.14,
    "deg": 140
  },
  "clouds": {
    "all": 75
  },
  "dt": 1757780497,
  "sys": {
    "type": 1,
    "id": 8394,
    "country": "BR",
    "sunrise": 1757754321,
    "sunset": 1757797186
  },
  "timezone": -10800,
  "id": 3448439,
  "name": "São Paulo",
  "cod": 200
}
```