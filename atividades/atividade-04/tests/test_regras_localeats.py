import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.regras_localeats import avaliacao_valida

def test_avaliacao_valida_com_nota_valida():
    resultado = avaliacao_valida(4)
    assert resultado is True

def test_avaliacao_invalida_acima_do_limite():
    resultado = avaliacao_valida(6)
    assert resultado is False

def test_avaliacao_com_tipo_invalido_lanca_excecao():
    with pytest.raises(TypeError):
        avaliacao_valida("excelente")