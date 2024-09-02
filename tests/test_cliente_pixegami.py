from unittest.mock import Mock

from sqlalchemy.orm import Session

from actions.clientes.service import ClienteService


def mock_get_cliente_by_cpf_cnpj(cpf_cnpj: str):
    if cpf_cnpj == '33199731856':
        return {
            'nome': "Natália Donato Benhossi",
            'cpf_cnpj': "33199731856",
            'tipo_pessoa': "FÍSICA"
        }
    else:
        return f'Dados do cliente {cpf_cnpj} não encontrados.'


def test_get_cliente_model_by_cpf_cnpj_succuess():
    cliente = ClienteService(Session)
    cliente.get_cliente_model_by_cpf_cnpj = Mock(side_effect=mock_get_cliente_by_cpf_cnpj)
    assert cliente.get_cliente_model_by_cpf_cnpj('33199731856') == {
                    'nome': "Natália Donato Benhossi",
                    'cpf_cnpj': "33199731856",
                    'tipo_pessoa': "FÍSICA"
                 }


def test_get_cliente_model_by_cpf_cnpj_not_found():
    cliente = ClienteService(Session)
    cliente.get_cliente_model_by_cpf_cnpj = Mock(side_effect=mock_get_cliente_by_cpf_cnpj)
    assert cliente.get_cliente_model_by_cpf_cnpj('12345678900') == 'Dados do cliente 12345678900 não encontrados.'


def test_get_cliente_model_by_cpf_cnpj_succuess():
    cliente = ClienteService(Session)
    cliente.get_cliente_dao_by_cpf_cnpj = Mock(side_effect=mock_get_cliente_by_cpf_cnpj)
    assert cliente.get_cliente_dao_by_cpf_cnpj('33199731856') == {
                    'nome': "Natália Donato Benhossi",
                    'cpf_cnpj': "33199731856",
                    'tipo_pessoa': "FÍSICA"
                 }
