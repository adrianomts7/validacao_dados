import pytest
from validacao_dados.models.endereco import Endereco
from validacao_dados.models.pessoa import Pessoa
from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa 

@pytest.fixture
def pessoa_valida():
    return Pessoa(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome))

def test_pessoa_id_valido(pessoa_valida):
    assert pessoa_valida.id == 12345

def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Adriano"
    
def test_pessoa_telefone_valido(pessoa_valida):
    assert pessoa_valida.telefone == "71976516212"
    
def test_pessoa_email_valido(pessoa_valida):
    assert pessoa_valida.email == "adriano@gmail.com"
    
def test_pessoa_id_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O id deve ser em numeros inteiros"):
        Pessoa("12345","Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome))
        
def test_pessoa_id_tipo_numero_negativo_retorna_mensagem():
    with pytest.raises(ValueError, match="O id não pode ser negativo"):
        Pessoa(-12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome))

def test_pessoa_nome_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O nome deve ser em texto"):
        Pessoa(12345,889,"71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome))

def test_pessoa_nome_tipo_vazio_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O nome não pode esta vazio"):
        Pessoa(12345," ","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome))
        
def test_pessoa_nome_tipo_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="Digite um nome com no minimo 3 letras"):
        Pessoa(12345,"AB","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome))
        
def test_pessoa_telefone_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O telefone deve ser em texto"):
        Pessoa(12345,"Adriano",71976516123,"adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome))
        
def test_pessoa_telefone_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="Digite o número com 11 digitos, incluindo o dd"):
        Pessoa(12345,"Adriano","719765","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome))
        
def test_pessoa_email_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O email deve ser em texto"):
        Pessoa(12345,"Adriano","71976509871",123098, Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome))
        
def test_pessoa_email_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O email deve ter no minino 15 digitos"):
         Pessoa(12345,"Adriano","71976509871","ano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome))