from common.connect_db import DbConnection
from source.actions.clientes.service import ClienteService

print(ClienteService(DbConnection().get_session()).get_cliente_dao_by_cpf_cnpj('33199731856'))
print(ClienteService(DbConnection().get_session()).get_cliente_model_by_cpf_cnpj('33199731856'))
