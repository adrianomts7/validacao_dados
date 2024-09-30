from validacao_dados.models.fornecedor import Fornecedor
from validacao_dados.models.endereco import Endereco
from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa

import pytest

@pytest.fixture
def fornecedor_valido():
    return Fornecedor(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa.BAHIA.nome),"18793871812","123456789","Computadores")
    
def test_forncedor_produto_valido(fornecedor_valido):
    assert fornecedor_valido.produto == "Computadores"
    
def test_forncedor_produto_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O produto tem que ser em texto"):
        Fornecedor(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa.BAHIA.nome),"18793871812","123456789",123)
        
def test_fornecedor_produto_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O produto tem que ter mais do que 3 letras"):
        Fornecedor(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa.BAHIA.nome),"18793871812","123456789","AB")