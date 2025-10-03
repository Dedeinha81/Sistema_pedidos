# 🛒 Sistemas de Pedidos

 
API RESTful desenvolvida em **Python** usando **FastAPI**, com **PostgreSQL** como banco de dados.  
Permite gerenciar clientes, produtos e pedidos de forma simples. ✅

---

## 💻 Tecnologias usadas

- 🐍 Python 3.13  
- ⚡ FastAPI  
- 🗄️ SQLAlchemy  
- 🛢️ PostgreSQL  
- 🚀 Uvicorn (servidor ASGI)  
- 📦 Pydantic  

---

## 🚀 Funcionalidades

- **Clientes**
  - 👥 Listar clientes
  - ➕ Criar cliente

- **Produtos**
  - 📦 Listar produtos
  - 🛍️ Criar produto

- **Pedidos**
  - 🧾 Listar pedidos
  - 🛒 Criar pedido

- **Rota raiz**
  - 🏠 Mensagem de boas-vindas

---

## 📦 Estrutura do projeto


Sistema_pedidos/
│

├── app.py              - Inicializa a API e define o roteamento principal

├── create_tables.py    - Criação das tabelas no banco de dados

├── database.py         - Configuração e conexão com PostgreSQL

├── models.py           - Modelos ORM com SQLAlchemy

├── crud.py             - Funções CRUD (Create e Read) para clientes, produtos e pedidos

├── routes.py           - Definição das rotas da API

├── schemas.py          - Schemas Pydantic para validação de dados

├── requirements.txt    - Lista de dependências do projeto

---

## ⚡ Instalação

1. Clone o repositório:

git clone [seu-link-do-repo]

cd Sistema_pedidos
---

Instale as dependências:

pip install -r requirements.txt

---

Configure a conexão com o PostgreSQL no database.py:

DATABASE_URL = "postgresql+psycopg2://postgres:SUA_SENHA@localhost:5432/sistema_pedidos"

---

Crie as tabelas no banco de dados:

python create_tables.py


⏳ As tabelas serão criadas automaticamente.

---

🏃‍♂️ Como rodar a API

uvicorn app:app --reload

---


Acesse a documentação interativa da API: http://127.0.0.1:8000/docs
 📝
 

🔗 Testando a API


GET /clientes/ → Lista todos os clientes 👥

POST /clientes/ → Cria um novo cliente ➕

GET /produtos/ → Lista todos os produtos 📦

POST /produtos/ → Cria um novo produto 🛍️

GET /pedidos/ → Lista todos os pedidos 🧾

POST /pedidos/ → Cria um novo pedido 🛒

Todos os endpoints usam JSON para entrada e saída de dados.

---

📝 Observações

Para rodar localmente, é necessário ter PostgreSQL instalado 🛢️.

---

🌐 Extras

Pode ser hospedado facilmente em serviços como Railway, Render ou Heroku para demonstração online 🌍.

Código organizado para fácil leitura, manutenção e expansão futura 🔧.

---

👩‍💻 Contato

Projeto criado por Andrea Cruz



