import pytest
# from pytest_mock import mocker
from sqlalchemy.orm import Session

import source.actions.clientes.dao.clientes
from actions.clientes.service import ClienteService


@pytest.fixture()
def mock_get_cliente_dao_by_cpf_cnpj(mocker):
    mock_get_cliente_dao_by_cpf_cnpj = mocker.patch(
        'source.actions.clientes.dao.clientes.ClienteDao.get_cliente_dao_by_cpf_cnpj')
    return mock_get_cliente_dao_by_cpf_cnpj


def test_get_cliente_dao_by_cpf_cnpj(mock_get_cliente_dao_by_cpf_cnpj):
    # session = mocker.MagicMock()
    mock_get_cliente_dao_by_cpf_cnpj.return_value = {
        'nome': 'John Doe',
        'cpf_cnpj': '1234567890123',
        'tipo_pessoa': 'Física'
    }

    service = ClienteService(Session)
    result = service.get_cliente_dao_by_cpf_cnpj('1234567890123')

    assert result == {
        'nome': 'John Doe',
        'cpf_cnpj': '1234567890123',
        'tipo_pessoa': 'Física'
    }
