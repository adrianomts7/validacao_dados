from validacao_dados.models.cliente import Cliente
from validacao_dados.models.endereco import Endereco
from validacao_dados.models.enums.estado_civil import EstadoCivil
from validacao_dados.models.enums.sexo import Sexo
from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa

import pytest

@pytest.fixture
def cliente_valido():
    return Cliente(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)

def test_cliente_protocolo_valido(cliente_valido):
    assert cliente_valido.protocoloAtendimento == 1234567891011
    
def test_cliente_protocoloAtendimento_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O protocolo de atendimento deve ser preenchido em números inteiros"):
         Cliente(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999","1234567891011")
         
def test_cliente_protocoloAtendimento_numero_negativo_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="Não pode digitar números negativos no protocolo de atendimento"):
        Cliente(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",-1234567891011)