from pydantic import BaseModel

class Produto(BaseModel):
    id_produto: int = None
    nome: str
    tipo: str
    valor: int