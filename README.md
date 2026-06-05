# AI Automation System

Sistema de automação desenvolvido com FastAPI, SQLAlchemy e SQLite para gerenciamento de tarefas automatizadas.

## Sobre o Projeto

O AI Automation System é uma API REST criada para demonstrar conceitos modernos de Engenharia de Software, desenvolvimento Backend e automação de processos.

O sistema permite criar, listar e atualizar tarefas, mantendo os dados persistidos em banco de dados SQLite.

## Tecnologias Utilizadas

* Python 3.14
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn
* Swagger/OpenAPI
* Git
* GitHub
- PostgreSQL-ready configuration
- psycopg2-binary

## Funcionalidades

### Criar Tarefas

```http
POST /automation/tasks
```

Permite cadastrar novas tarefas com:

* Título
* Descrição
* Prioridade
* Status

### Listar Tarefas

```http
GET /automation/tasks
```

Retorna todas as tarefas cadastradas.

### Atualizar Status

```http
PUT /automation/tasks/{task_id}/status
```

Permite alterar o status de uma tarefa.

Exemplos:

* pending
* running
* completed
* failed

## Estrutura do Projeto

```text
backend/
│
├── app/
│   ├── main.py
│   ├── database.py
│   └── models.py
│
├── requirements.txt
└── Dockerfile
```

## Executando o Projeto

## Configuração de Ambiente

O projeto utiliza variáveis de ambiente para facilitar a troca entre bancos de dados.

Exemplo de configuração SQLite:

```env
DATABASE_URL=sqlite:///./automation.db
APP_NAME=AI Automation System
APP_VERSION=3.1.0

### Instalar Dependências

```bash
pip install -r requirements.txt
```

### Executar a API

```bash
python -m uvicorn app.main:app --reload
```

### Abrir Swagger

```text
http://127.0.0.1:8000/docs
```

## Próximas Implementações

* DELETE de tarefas
* Consulta individual de tarefas
* Validação de status
* Autenticação JWT
* PostgreSQL
* Frontend React
* Integração com Inteligência Artificial

## Autor

Helton Santos

Software Engineer Student | Artificial Intelligence | Automation Systems | Cybersecurity

GitHub: https://github.com/helton-IA

