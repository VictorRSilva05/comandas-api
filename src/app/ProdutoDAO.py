#Victor Rafael da Silva
from fastapi import APIRouter
from domain.entities.Produto import	Produto

import db
from infra.orm.ProdutoModel import ProdutoDB

router = APIRouter()

@router.get("/produto/", tags=["Produto"])
async def get_produto():
    try:
        session = db.Session()
        
        # busca todos
        dados = session.query(ProdutoDB).all()
        
        return dados, 200
    
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()
        
@router.get("/produto/{id}", tags=["Produto"])
async def get_produto(id: int):
    try:
        session = db.Session()

        # busca um com filtro
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).all()

        return dados, 200

    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/produto/", tags=["Produto"])
async def post_produto(corpo: Produto):
    try:
        session = db.Session()
    
        # cria um novo objeto com os dados da requisição
        dados = ProdutoDB(None, corpo.nome, corpo.tipo, corpo.valor)

        session.add(dados)
        # session.flush()
        session.commit()
        
        return {"id": dados.id_produto}, 200
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()
        
@router.put("/produto/{id}", tags=["Produto"])
async def put_produto(id: int, corpo: Produto):
    try:
        session = db.Session()
        # busca os dados atuais pelo id
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        # atualiza os dados com base no corpo da requisição
        dados.nome = corpo.nome
        dados.tipo = corpo.tipo
        dados.valor = corpo.valor
        session.add(dados)
        session.commit()
        
        return {"id": dados.id_funcionario}, 200
        
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

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