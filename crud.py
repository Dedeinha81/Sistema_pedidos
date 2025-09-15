
from sqlalchemy.orm import Session
import models, schemas

# Funções para clientes
def criar_cliente(db: Session, cliente: schemas.ClienteCreate):
    novo_cliente = models.Cliente(nome=cliente.nome, email=cliente.email)
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente

def listar_clientes(db: Session):
    return db.query(models.Cliente).all()

# Funções para produtos
def criar_produto(db: Session, produto: schemas.ProdutoCreate):
    novo_produto = models.Produto(nome=produto.nome, preco=produto.preco)
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

def listar_produtos(db: Session):
    return db.query(models.Produto).all()

# Funções para pedidos
def criar_pedido(db: Session, pedido: schemas.PedidoCreate):
    novo_pedido = models.Pedido(cliente_id=pedido.cliente_id, produto_id=pedido.produto_id)
    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)
    return novo_pedido

def listar_pedidos(db: Session):
    return db.query(models.Pedido).all()
