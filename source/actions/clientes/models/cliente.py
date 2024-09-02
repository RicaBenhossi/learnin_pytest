from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Cliente(Base):

    __tablename__ = "clientes"

    id = Column(String(16), primary_key=True)
    nome = Column(String(100))
    cpf_cnpj = Column(String(14))
    tipo_pessoa = Column(String)
