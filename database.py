
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão com PostgreSQL local
# Substitua 'usuario' e 'senha' pelos que você criou na instalação do PostgreSQL
DATABASE_URL = "postgresql+psycopg2://postgres:150525@localhost:5432/sistema_pedidos"

# Criar engine de conexão com o banco
engine = create_engine(DATABASE_URL)

# Criar sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()

