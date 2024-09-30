from validacao_dados.models.fisica import Fisica
from validacao_dados.models.endereco import Endereco
from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa
from validacao_dados.models.enums.sexo import Sexo
from validacao_dados.models.enums.estado_civil import EstadoCivil


import pytest

@pytest.fixture
def fisica_valida():
    return Fisica(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999")

def test_fisica_dataNascimento_valida(fisica_valida):
    assert fisica_valida.dataNascimento == "20/10/1999"

def test_enum_sexo_validos():
    Sexo.MASCULINO.name == "Masculino"
    Sexo.FEMININO.name == "FEMININO"
    
def test_enum_estadoCivil_validos():
    EstadoCivil.SOLTEIRO.name == "Solteiro"
    EstadoCivil.CASADO.name == "CASADO"
    EstadoCivil.SEPARADO.name == "SEPARADO"
    EstadoCivil.VIUVO.name == "VIUVO"
    EstadoCivil.DIVORCIO.name == "Divorciado"
    
def test_fisica_dataNascimento_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="A data nascimento deve ser em texto"):
        Fisica(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,20101999)
        
def test_fisica_dataNascimento_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="A data de nascimento deve conter 10 digitos junto com '/'"):
        Fisica(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20101999")