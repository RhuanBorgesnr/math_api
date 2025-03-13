
## Visão Geral

A **Math API** é uma API RESTful desenvolvida em Django que fornece operações matemáticas básicas: **soma** e **média** de um vetor de números. Além disso, a API registra o histórico de cálculos em um banco de dados PostgreSQL.

### Funcionalidades

- **Soma**: Soma todos os números de um array.
- **Média**: Calcula a média aritmética dos números em um array.
- **Histórico**: Registra cada operação com detalhes como tipo de operação, números de entrada, resultado e data/hora.

## Requisitos

- Python 3.8+
- Django 3.2+ e Django REST Framework
- Docker e Docker Compose (para PostgreSQL)
- PostgreSQL (executando via Docker ou instalado localmente)

## Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/math_api.git
cd math_api
```

### 2. Configurar um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

## Configuração do Banco de Dados com Docker

Para armazenar o histórico de cálculos, utilize o Docker Compose para iniciar um contêiner PostgreSQL. Certifique-se de que o seguinte arquivo `docker-compose.yml` esteja na raiz do projeto:

```yaml
version: "3"
services:
  postgres:
    image: postgres:13
    container_name: math_api_postgres
    restart: always
    environment:
      POSTGRES_DB: math_api_db
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass123
    ports:
      - "5432:5432"
```

### Iniciar o Contêiner do Banco de Dados

```bash
docker-compose up -d
```

## Configuração do Django

Modifique o arquivo `settings.py` para configurar o PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'math_api_db',
        'USER': 'user',
        'PASSWORD': 'pass123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Aplicar Migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

## Executando o Servidor

Inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

A API estará disponível em [http://localhost:8000](http://localhost:8000).

## Documentação da API

### Endpoints

#### 1. Soma

**Endpoint:** `POST /api/calculator/sum/`

**Corpo da Requisição (JSON):**

```json
{
  "numbers": [1, 2, 3, 4]
}
```

**Resposta (JSON):**

```json
{
  "result": 10
}
```

#### 2. Média

**Endpoint:** `POST /api/calculator/average/`

**Corpo da Requisição (JSON):**

```json
{
  "numbers": [1, 2, 3, 4]
}
```

**Resposta (JSON):**

```json
{
  "result": 2.5
}
```

#### 2. Histórico de cálculos

**Endpoint:** `GET /api/calculator/history/`

**Corpo da Requisição (JSON):**

**Resposta (JSON):**

```json
{
  "history": [
    {
      "id": 1,
      "operation": "average",
      "input_numbers": "[1, 2, 3, 4]",
      "result": 2.5,
      "created_at": "2025-03-13T12:04:58.740685Z"
    }
  ]
}
```

## Exemplos de Requisições Usando cURL

### Soma

```bash
curl -X POST   -H "Content-Type: application/json"   -d '{"numbers": [1, 2, 3, 4]}'   http://localhost:8000/api/calculator/sum/
```

### Média

```bash
curl -X POST   -H "Content-Type: application/json"   -d '{"numbers": [1, 2, 3, 4]}'   http://localhost:8000/api/calculator/average/
```

## Executando Testes

Testes unitários foram implementados para classes e endpoints. Execute-os usando:

```bash
python manage.py test
```
