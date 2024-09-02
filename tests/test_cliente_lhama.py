from unittest import mock

from sqlalchemy.orm import Session
from source.actions.clientes.service import ClienteService
from actions.clientes.dao.clientes import ClienteDao
from source.actions.clientes.models.cliente import Cliente
from mock_alchemy.mocking import UnifiedAlchemyMagicMock


session = UnifiedAlchemyMagicMock(
    data=[
        (
            [
                mock.call.query(Cliente),
                mock.call.filter(Cliente.cpf_cnpj=='33199731856')
            ],
            [
                Cliente(id=b'1234', nome="Natália Donato Benhossi", cpf_cnpj="33199731856", tipo_pessoa="FÍSICA")
                # {
                #     'nome': "Natália Donato Benhossi",
                #     'cpf_cnpj': "33199731856",
                #     'tipo_pessoa': "FÍSICA"
                #  }
            ]
        )
    ]
)


def test_find_cliente_by_cnpj_cpf():
    # response = ClienteService(session).get_cliente_model_by_cpf_cnpj('33199731856')
    response = session.query(Cliente).filter_by(cpf_cnpj='33199731856').one()
    assert response == {
                    'nome': "Natália Donato Benhossi",
                    'cpf_cnpj': "33199731856",
                    'tipo_pessoa': "FÍSICA"
                 }


session2 = UnifiedAlchemyMagicMock(
    data=[
        (
            [
                mock.call.ClienteDao.execute
            ],
            [
                # Cliente(nome="Natália Donato Benhossi", cpf_cnpj="33199731856", tipo_pessoa="FÍSICA")
                {
                    'nome': "Natália Donato Benhossi",
                    'cpf_cnpj': "33199731856",
                    'tipo_pessoa': "FÍSICA"
                 }
            ]
        )
    ]
)


def test_find_cliente_by_cnpj_cpf_dao():
    # response = session2.get_cliente_dao_by_cpf_cnpj('33199731856')
    response = ClienteDao(session2).get_cliente_dao_by_cpf_cnpj('33199731856')
    assert response == {
                    'nome': "Natália Donato Benhossi",
                    'cpf_cnpj': "33199731856",
                    'tipo_pessoa': "FÍSICA"
                 }
