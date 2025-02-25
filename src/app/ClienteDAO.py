#Victor Rafael da Silva
from fastapi import APIRouter
from domain.entities.Cliente import Cliente

import db
from infra.orm.ClienteModel import ClienteDB

router = APIRouter()

@router.get("/cliente/", tags=["Cliente"])
async def get_client():
    try:
        session = db.Session()
        
        #busca todos
        dados = session.query(ClienteDB).all()
        
        return dados, 200
    
    except Exception as e:
        return{"erro": str(e)}, 400
    finally:
        session.close()
        
@router.get("/cliente/{id}", tags=["Cliente"])
async def get_cliente(id: int):
    try:
        session = db.Session()

        # busca um com filtro
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).all()

        return dados, 200

    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()
        
@router.post("/cliente/", tags=["Cliente"])
async def post_cliente(corpo: Cliente):
    try:
        session = db.Session()
    
        # cria um novo objeto com os dados da requisição
        dados = ClienteDB(None, corpo.nome, corpo.cpf, corpo.telefone)

        session.add(dados)
        # session.flush()
        session.commit()
        
        return {"id": dados.id_cliente}, 200
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/cliente/{id}", tags=["Cliente"])
async def put_cliente(id: int, corpo: Cliente):
    try:
        session = db.Session()
        # busca os dados atuais pelo id
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one()
        # atualiza os dados com base no corpo da requisição
        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.telefone = corpo.telefone
        
        session.add(dados)
        session.commit()
        
        return {"id": dados.id_cliente}, 200
        
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()
        
@router.put("/cliente/{id}", tags=["Cliente"])
async def put_cliente(id: int, corpo: Cliente):
    try:
        session = db.Session()
        # busca os dados atuais pelo id
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one()
        # atualiza os dados com base no corpo da requisição
        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.telefone = corpo.telefone
        session.add(dados)
        session.commit()
        
        return {"id": dados.id_cliente}, 200
        
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()
        
# verifica se o CPF informado já esta cadastrado, retornado os dados atuais caso já esteja
@router.get("/cliente/cpf/{cpf}", tags=["Cliente - Valida CPF"])
async def cpf_cliente(cpf: str):
    try:
        session = db.Session()
        
        # busca um com filtro, retornando os dados cadastrados
        dados = session.query(ClienteDB).filter(ClienteDB.cpf == cpf).all()
        
        return dados, 200
    
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()
        
# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/cliente/", tags=["Cliente"])
async def get_cliente():
    return {"msg": "get todos executado"}, 200

@router.get("/cliente/{id}", tags=["Cliente"])
async def get_cliente(id: int):
    return {"msg": "get um executado"}, 200

@router.post("/cliente/", tags=["Cliente"])
async def post_cliente(corpo: Cliente):
    return {"msg": "post executado", "nome": corpo.nome, "cpf": corpo.cpf, "telefone": corpo.telefone}, 200

@router.put("/cliente/{id}", tags=["Cliente"])
async def put_cliente(id: int, corpo: Cliente):
    return {"msg": "put executado", "id":id, "nome": corpo.nome, "cpf": corpo.cpf, "telefone": corpo.telefone}, 200

@router.delete("/cliente/{id}", tags=["Cliente"])
async def delete_cliente(id: int):
    return {"msg": "delete executado", "id":id}, 200