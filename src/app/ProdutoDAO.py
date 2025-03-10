#Victor Rafael da Silva
from fastapi import APIRouter
from domain.entities.Produto import	Produto

import db
from infra.orm.ProdutoModel import ProdutoDB

# import da segurança
from typing import Annotated
from fastapi import Depends
from security import get_current_active_user, User

router = APIRouter(dependencies=[Depends(get_current_active_user)])

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
        
        return {"id": dados.id_produto}, 200
        
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()
        
@router.delete("/produto/{id}"  )
async def delete_produto(id: int):
    try:
        session = db.Session()
        produto = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).first()

        if not produto:
            return {"erro": "Produto não encontrado"}, 404

        session.delete(produto)
        session.commit()
        return {"mensagem": "Produto deletado com sucesso"}, 200

    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()