from sqlalchemy import text
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from common.connect_db import DbConnection


class ClienteDao:
    def __init__(self, session: Session):
        self.__session = session

    def get_cliente_dao_by_cpf_cnpj(self, cpf_cnpj: str) -> dict:
        query = 'select nome, cpf_cnpj, tipo_pessoa ' \
                '  from clientes' \
                ' where cpf_cnpj = :cpf_cnpj'

        params = {'cpf_cnpj': cpf_cnpj}

        try:
            data = self.__session.execute(text(query), params)

            return data.mappings().one()

        except NoResultFound as e:
            return f'Dados do cliente {cpf_cnpj} não encontrados.'
