
from fastapi import FastAPI
import models
from database import engine
import routes

# Criar tabelas automaticamente
models.Base.metadata.create_all(bind=engine)

# Criar app FastAPI
app = FastAPI(title="Sistemas de pedidos")

# Incluir rotas
app.include_router(routes.router)

@app.get("/")
def raiz():
    return {"mensagem":"Bem vindo ao Sistema de pedidos!"}