
from database import engine, Base
import models

# Cria todas as tabelas no banco de dados
print("⏳ Criando tabelas no banco...")
Base.metadata.create_all(bind=engine)
print("✅ Tabelas criadas com sucesso!")
