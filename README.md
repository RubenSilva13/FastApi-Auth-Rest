# FastAPI Auth — REST API

API REST com autenticação JWT e gestão de tarefas, construída com FastAPI e MySQL.

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python_3.13-3776AB?style=flat&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=flat&logo=jsonwebtokens&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

<!-- Opcional: arrasta aqui um screenshot do Swagger (http://localhost:8000/docs) -->

## 🛠️ Tecnologias

- Python 3.13
- FastAPI
- SQLAlchemy
- MySQL
- JWT (python-jose)
- bcrypt (passlib)
- Docker / Docker Compose

## ✨ Funcionalidades

- Registo e login de utilizadores
- Autenticação com token JWT
- Endpoints protegidos por autenticação
- Passwords encriptadas com bcrypt
- CRUD de tarefas com filtros por estado e prioridade

## 📡 Endpoints

### Autenticação
| Método | Endpoint | Descrição | Auth |
|--------|----------|-----------|------|
| POST | /auth/register | Criar conta | Não |
| POST | /auth/login | Login e obter token | Não |
| GET | /auth/me | Ver perfil | Sim |

### Tarefas
| Método | Endpoint | Descrição | Auth |
|--------|----------|-----------|------|
| POST | /tasks/ | Criar tarefa | Sim |
| GET | /tasks/ | Listar tarefas | Sim |
| GET | /tasks/?completed=false | Filtrar por estado | Sim |
| GET | /tasks/?priority=alta | Filtrar por prioridade | Sim |
| GET | /tasks/{id} | Ver tarefa | Sim |
| PUT | /tasks/{id} | Atualizar tarefa | Sim |
| DELETE | /tasks/{id} | Apagar tarefa | Sim |

Com a API a correr, a documentação interativa (Swagger) fica em `http://localhost:8000/docs`.

## 🚀 Como correr localmente

### Opção A — Docker (recomendado)

Sobe a API e o MySQL juntos, sem instalar mais nada além do Docker:

```bash
git clone https://github.com/RubenSilva13/FastApi-Auth-Rest
cd FastApi-Auth-Rest
docker compose up --build
```

A API fica em `http://localhost:8000` e o Swagger em `http://localhost:8000/docs`.

### Opção B — Manual (sem Docker)

Requer Python 3.11+ e uma base de dados MySQL a correr.

```bash
git clone https://github.com/RubenSilva13/FastApi-Auth-Rest
cd FastApi-Auth-Rest
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Cria um ficheiro `.env` na raiz com:

```
DATABASE_URL=mysql+pymysql://root:@localhost:3306/minhaapi
SECRET_KEY=a-tua-chave-secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 📂 Estrutura

```
app/
├── main.py         # App FastAPI, CORS e arranque
├── database.py     # Ligação à base de dados (SQLAlchemy)
├── models.py       # Modelos (utilizadores e tarefas)
├── schemas.py      # Schemas Pydantic
├── auth.py         # JWT e hashing de passwords
└── routers/
    ├── auth.py     # Rotas de autenticação
    └── tasks.py    # Rotas de tarefas
Dockerfile
docker-compose.yml
requirements.txt
```

## 🔗 Relacionado

- **Frontend (React):** [FastApi-Auth-React](https://github.com/RubenSilva13/FastApi-Auth-React)
