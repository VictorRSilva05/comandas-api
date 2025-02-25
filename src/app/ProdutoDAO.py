#Victor Rafael da Silva
from fastapi import APIRouter
from domain.entities.Produto import	Produto

import db
from infra.orm.ProdutoModel import ProdutoDB

router = APIRouter()

@router.get("/produto/", tags=["Produto"])
async def get_produto():
    return {"msg": "get todos executado"}, 200

@router.get("/produto/{id}", tags=["Produto"])
async def get_produto(id: int):
    return{"msg": "get um executado"}, 200

@router.post("/produto/", tags=["Produto"])
async def post_produto(corpo: Produto):
    return {"msg": "post executado", "nome": corpo.nome, "tipo": corpo.tipo, "valor":corpo.valor}, 200

@router.put("/produto/{id}", tags=["Produto"])
async def put_produto(id: int, corpo: Produto):
    return {"msg": "put executado", "nome": corpo.nome, "tipo": corpo.tipo, "valor":corpo.valor}, 200

@router.delete("/produto/{id}", tags=["Produto"])
async def delete_produto(id: int):
    return {"msg": "delete executado"}, 200