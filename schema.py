"""Arquivo de Contrato de Dados."""

from datetime import datetime

from pydantic import BaseModel, EmailStr, PositiveInt


class ContratoFuncionarios(BaseModel):
    """Classe de Contrato de Dados.

    Args:
        id (PositiveInt): Identificador do registro
        nome (str): Nome do funcionário
        idade (PositiveInt): Idade do funcionário
        datanascimento (datetime): Data de nascimento do funcionário
        email (EmailStr): Email do funcionário
        cargo (str): Cargo do funcionário
        departamento (str): Departamento do funcionário
    """

    id: PositiveInt
    nome: str
    idade: PositiveInt
    datanascimento: datetime
    email: EmailStr
    cargo: str
    departamento: str
