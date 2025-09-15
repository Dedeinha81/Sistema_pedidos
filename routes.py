
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas
from database import SessionLocal

router = APIRouter()

# Dependência para criar sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rotas Clientes
@router.post("/clientes/", response_model=schemas.ClienteOut)
def criar_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.criar_cliente(db, cliente)

@router.get("/clientes/", response_model=list[schemas.ClienteOut])
def listar_clientes(db: Session = Depends(get_db)):
    return crud.listar_clientes(db)

# Rotas Produtos
@router.post("/produtos/", response_model=schemas.ProdutoOut)
def criar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    return crud.criar_produto(db, produto)

@router.get("/produtos/", response_model=list[schemas.ProdutoOut])
def listar_produtos(db: Session = Depends(get_db)):
    return crud.listar_produtos(db)

# Rotas Pedidos
@router.post("/pedidos/", response_model=schemas.PedidoOut)
def criar_pedido(pedido: schemas.PedidoCreate, db: Session = Depends(get_db)):
    return crud.criar_pedido(db, pedido)

@router.get("/pedidos/", response_model=list[schemas.PedidoOut])
def listar_pedidos(db: Session = Depends(get_db)):
    return crud.listar_pedidos(db)
