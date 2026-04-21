# FastAPI Auth REST

API REST com autenticação JWT construída com FastAPI e MySQL.

## Tecnologias
- Python 3.13
- FastAPI
- SQLAlchemy
- MySQL
- JWT (python-jose)
- bcrypt (passlib)

## Funcionalidades
- Registo de utilizadores
- Login com token JWT
- Endpoint protegido com autenticação
- Passwords encriptadas com bcrypt

## Como correr localmente

### Pré-requisitos
- Python 3.11+
- MySQL a correr (WampServer ou similar)

### Instalação

1. Clona o repositório
git clone https://github.com/RubenSilva13/FastApi-Auth-Rest.git

2. Cria e ativa o virtual environment
python -m venv venv
venv\Scripts\activate

3. Instala as dependências
pip install -r requirements.txt

4. Cria o ficheiro .env com as tuas configurações
DATABASE_URL=mysql+pymysql://root:@localhost:3306/minhaapi
SECRET_KEY=a-tua-chave-secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

5. Corre a API
uvicorn app.main:app --reload

## Documentação
Com a API a correr, acede a http://127.0.0.1:8000/docs para ver a documentação interativa.

## Endpoints
| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
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
| DELETE | /tasks/{id} | Apagar tarefa | Sim 