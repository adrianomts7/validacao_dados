from validacao_dados.models.fornecedor import Fornecedor
from validacao_dados.models.endereco import Endereco
from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa

import pytest

@pytest.fixture
def fornecedor_valido():
    return Fornecedor(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa.BAHIA.nome),"18793871812","123456789","Computadores")
    
def test_forncedor_produto_valido(fornecedor_valido):
    assert fornecedor_valido.produto == "Computadores"
    
def test_pessoa_id_valido(fornecedor_valido):
    assert fornecedor_valido.id == 1234

def test_pessoa_nome_valido(fornecedor_valido):
    assert fornecedor_valido.nome == "Adriano"
    
def test_pessoa_telefone_valido(fornecedor_valido):
    assert fornecedor_valido.telefone == "71917268176"
    
def test_pessoa_email_valido(fornecedor_valido):
    assert fornecedor_valido.email == "adriano@gmail.com"

def test_juridica_cnpj_valido(fornecedor_valido):
    assert fornecedor_valido.cnpj == "18793871812"
    
def test_juridica_incricao_estadual_valido(fornecedor_valido):
    assert fornecedor_valido.incricaoEstadual == "123456789"
    
def test_pessoa_id_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O id deve ser em numeros inteiros"):
        Fornecedor("12345","Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),"18793871812","123456789","Computadores")
        
def test_pessoa_id_tipo_numero_negativo_retorna_mensagem():
    with pytest.raises(ValueError, match="O id não pode ser negativo"):
        Fornecedor(-12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),"18793871812","123456789","Computadores")

def test_pessoa_nome_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O nome deve ser em texto"):
        Fornecedor(12345,889,"71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),"18793871812","123456789","Computadores")

def test_pessoa_nome_tipo_vazio_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O nome não pode esta vazio"):
        Fornecedor(12345," ","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),"18793871812","123456789","Computadores")
        
def test_pessoa_nome_tipo_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="Digite um nome com no minimo 3 letras"):
        Fornecedor(12345,"AB","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),"18793871812","123456789","Computadores")
        
def test_pessoa_telefone_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O telefone deve ser em texto"):
        Fornecedor(12345,"Adriano",71976516123,"adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),"18793871812","123456789","Computadores")
        
def test_pessoa_telefone_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="Digite o número com 11 digitos, incluindo o dd"):
        Fornecedor(12345,"Adriano","719765","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),"18793871812","123456789","Computadores")
        
def test_pessoa_email_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O email deve ser em texto"):
        Fornecedor(12345,"Adriano","71976509871",123098, Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),"18793871812","123456789","Computadores")
        
def test_pessoa_email_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O email deve ter no minino 15 digitos"):
         Fornecedor(12345,"Adriano","71976509871","ano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),"18793871812","123456789","Computadores")


def test_juridica_cnpj_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O Cnpj deve ser em texto"):
        Fornecedor(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),18793871812,"123456789","Computadores")
        
def test_juridica_cnpj_tamanho_invalida_retorna_mensagem():
    with pytest.raises(ValueError, match="O cnpj deve conter no minimo 9 digitos"):
        Fornecedor(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),"1879387","123456789","Computadores")
        
def test_juridico_incricaoEstadual_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="A incrição estadual deve ser em texto"):
        Fornecedor(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),"187938789",123456789,"Computadores")
        
def test_juridico_inscricaoEstadual_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="A inscrição estadual deve conter 9 digitos"):
        Fornecedor(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),"187938789","1234567","Computadores")

def test_forncedor_produto_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O produto tem que ser em texto"):
        Fornecedor(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa.BAHIA.nome),"18793871812","123456789",123)
        
def test_fornecedor_produto_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O produto tem que ter mais do que 3 letras"):
        Fornecedor(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa.BAHIA.nome),"18793871812","123456789","Co")
