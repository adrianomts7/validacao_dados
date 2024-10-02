from validacao_dados.models.cliente import Cliente
from validacao_dados.models.endereco import Endereco
from validacao_dados.models.enums.estado_civil import EstadoCivil
from validacao_dados.models.enums.sexo import Sexo
from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa
from validacao_dados.models.enums.setor import Setor

import pytest

@pytest.fixture
def cliente_valido():
    return Cliente(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)


def test_pessoa_id_valido(cliente_valido):
    assert cliente_valido.id == 12345

def test_pessoa_nome_valido(cliente_valido):
    assert cliente_valido.nome == "Adriano"
    
def test_pessoa_telefone_valido(cliente_valido):
    assert cliente_valido.telefone == "71976516212"
    
def test_pessoa_email_valido(cliente_valido):
    assert cliente_valido.email == "adriano@gmail.com"

def test_fisica_dataNascimento_valida(cliente_valido):
    assert cliente_valido.dataNascimento == "20/10/1999"

def test_cliente_protocolo_valido(cliente_valido):
    assert cliente_valido.protocoloAtendimento == 1234567891011
    
def test_enum_sexo_validos():
    Sexo.MASCULINO.name == "Masculino"
    Sexo.FEMININO.name == "FEMININO"
    
def test_enum_estadoCivil_validos():
    EstadoCivil.SOLTEIRO.name == "Solteiro"
    EstadoCivil.CASADO.name == "CASADO"
    EstadoCivil.SEPARADO.name == "SEPARADO"
    EstadoCivil.VIUVO.name == "VIUVO"
    EstadoCivil.DIVORCIO.name == "Divorciado"

def test_pessoa_id_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O id deve ser em numeros inteiros"):
         Cliente("12345","Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)
        
def test_pessoa_id_tipo_numero_negativo_retorna_mensagem():
    with pytest.raises(ValueError, match="O id não pode ser negativo"):
         Cliente(-12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)

def test_pessoa_nome_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O nome deve ser em texto"):
         Cliente(12345,889,"71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)

def test_pessoa_nome_tipo_vazio_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O nome não pode esta vazio"):
         Cliente(12345," ","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)
        
def test_pessoa_nome_tipo_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="Digite um nome com no minimo 3 letras"):
         Cliente(12345,"AB","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)
        
def test_pessoa_telefone_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O telefone deve ser em texto"):
         Cliente(12345,"Adriano",71976516123,"adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)
        
def test_pessoa_telefone_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="Digite o número com 11 digitos, incluindo o dd"):
        Cliente(12345,"Adriano","719765","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)
        
def test_pessoa_email_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O email deve ser em texto"):
         Cliente(12345,"Adriano","71976509871",123098, Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)
        
def test_pessoa_email_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O email deve ter no minino 15 digitos"):
          Cliente(12345,"Adriano","71976509871","ano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)

def test_fisica_dataNascimento_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="A data nascimento deve ser em texto"):
         Cliente(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,20101999,1234567891011)
        
def test_fisica_dataNascimento_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="A data de nascimento deve conter 10 digitos junto com '/'"):
        Cliente(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20101999",1234567891011)
    
def test_cliente_protocoloAtendimento_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O protocolo de atendimento deve ser preenchido em números inteiros"):
         Cliente(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999","1234567891011")
         
def test_cliente_protocoloAtendimento_numero_negativo_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="Não pode digitar números negativos no protocolo de atendimento"):
        Cliente(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",-1234567891011)