
from pydantic import BaseModel

# Schemas para Cliente
class ClienteBase(BaseModel):
    nome: str
    email: str

class ClienteCreate(ClienteBase):
    pass

class ClienteOut(ClienteBase):
    id: int
    class Config:
        orm_mode = True

# Schemas para Produto
class ProdutoBase(BaseModel):
    nome: str
    preco: float

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoOut(ProdutoBase):
    id: int
    class Config:
        orm_mode = True

# Schemas para Pedido
class PedidoBase(BaseModel):
    cliente_id: int
    produto_id: int

class PedidoCreate(PedidoBase):
    pass

class PedidoOut(PedidoBase):
    id: int
    class Config:
        orm_mode = True
