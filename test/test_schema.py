"""Arquivo de testes do schema."""

from datetime import datetime

import pytest
from pydantic import ValidationError

from schema import ContratoFuncionarios


def test_validar_contrato():
    """Testa se o schema de dados é valido."""
    dados_validos = {
        "id": 1,
        "nome": "Luciano Borba",
        "idade": 23,
        "datanascimento": datetime.now(),
        "email": "luhborbafilho@gmail.com",
        "cargo": "Desenvolvedor Python",
        "departamento": "TI",
    }
    funcionarios = ContratoFuncionarios(**dados_validos)
    assert funcionarios.id == dados_validos["id"]
    assert funcionarios.nome == dados_validos["nome"]
    assert funcionarios.idade == dados_validos["idade"]
    assert funcionarios.datanascimento == dados_validos["datanascimento"]
    assert funcionarios.email == dados_validos["email"]
    assert funcionarios.cargo == dados_validos["cargo"]
    assert funcionarios.departamento == dados_validos["departamento"]


def test_dados_invalidos():
    """Testa se o schema de dados é invalido."""
    dados_invalidos = {
        "id": -1,
        "nome": "Luciano Borba",
        "idade": 23,
        "datanascimento": datetime.now(),
        "email": "luhborbafilho",
        "cargo": "Desenvolvedor Python",
        "departamento": "TI",
    }
    with pytest.raises(ValidationError):
        ContratoFuncionarios(**dados_invalidos)
