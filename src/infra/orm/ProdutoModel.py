import db
from sqlalchemy import Column, VARCHAR, DECIMAL, Integer

class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'
    
    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    tipo = Column(VARCHAR(100), nullable=False)
    valor = Column(DECIMAL(10,2), nullable=False)
    
    def __init__(self, id_produto, nome, tipo, valor):
        self.id_produto = id_produto
        self.nome = nome
        self.tipo = tipo
        self.valor = valor
    