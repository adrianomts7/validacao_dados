from validacao_dados.models.endereco import Endereco
from validacao_dados.models.juridica import Juridica
from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa

import pytest

@pytest.fixture
def juridica_valida():
    return Juridica(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),"18793871812","123456789")

def test_juridica_cnpj_valido(juridica_valida):
    assert juridica_valida.cnpj == "18793871812"
    
def test_juridica_incricao_estadual_valido(juridica_valida):
    assert juridica_valida.incricaoEstadual == "123456789"
    
def test_juridica_cnpj_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O Cnpj deve ser em texto"):
        Juridica(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),18793871812,"123456789")
        
def test_juridica_cnpj_tamanho_invalida_retorna_mensagem():
    with pytest.raises(ValueError, match="O cnpj deve conter no minimo 9 digitos"):
        Juridica(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),"1879387","123456789")
        
def test_juridico_incricaoEstadual_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="A incrição estadual deve ser em texto"):
        Juridica(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),"187938789",123456789)
        
def test_juridico_inscricaoEstadual_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="A inscrição estadual deve conter 9 digitos"):
        Juridica(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),"187938789","1234567")