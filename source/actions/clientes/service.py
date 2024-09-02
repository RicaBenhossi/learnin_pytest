from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from actions.clientes.dao.clientes import ClienteDao
from actions.clientes.models.cliente import Cliente
from source.common.connect_db import DbConnection


class ClienteService:
    def __init__(self, session: Session):
        self.__session = session

    def get_cliente_model_by_cpf_cnpj(self, cpf_cnpj: str) -> dict:
        try:
            cliente: Cliente = self.__session.query(Cliente).filter_by(cpf_cnpj=cpf_cnpj).one()
        except NoResultFound as e:
            return f'Dados do cliente {cpf_cnpj} não encontrados.'

        return {column.name: getattr(cliente, column.name) for column in Cliente.__table__.columns}
        # return {
        #     'nome': cliente.nome,
        #     'cpf_cnpj': cliente.cpf_cnpj,
        #     'tipo_pessoa': cliente.tipo_pessoa
        # }

    def get_cliente_dao_by_cpf_cnpj(self, cpf_cnpj: str) -> dict:
        return ClienteDao(self.__session).get_cliente_dao_by_cpf_cnpj(cpf_cnpj)
