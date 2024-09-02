from unittest.mock import patch

from sqlalchemy.orm import Session

import source.actions.clientes.service
from source.actions.clientes.service import ClienteService


@patch('source.actions.clientes.service.ClienteService.get_cliente_model_by_cpf_cnpj')
def test_get_cliente_model_by_cpf_cnpj(mock_get):
    mock_get.return_value = {
                    'nome': "Natália Donato Benhossi",
                    'cpf_cnpj': "33199731856",
                    'tipo_pessoa': "FÍSICA"
                 }
    assert ClienteService(Session).get_cliente_dao_by_cpf_cnpj('33199731856') == {
                    'nome': "Natália Donato Benhossi",
                    'cpf_cnpj': "33199731856",
                    'tipo_pessoa': "FÍSICA"
                 }
