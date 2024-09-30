from validacao_dados.models.engenheiro import Engenheiro
from validacao_dados.models.endereco import Endereco
from validacao_dados.models.enums.estado_civil import EstadoCivil
from validacao_dados.models.enums.sexo import Sexo
from validacao_dados.models.enums.setor import Setor
from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa

import pytest

@pytest.fixture
def engenheiro_valido():
    return Engenheiro(231,"Marta","71982718293","marta@gmail.com",Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","01923102310","237189201","3001",Setor.ENGENHARIA.name,8950.70,"Crea-BA")

def test_engenheiro_valido(engenheiro_valido):
    assert engenheiro_valido.id == 231
    assert engenheiro_valido.nome == "Marta"
    assert engenheiro_valido.telefone == "71982718293"
    assert engenheiro_valido.email == "marta@gmail.com"
    assert engenheiro_valido.endereco.logradouro == "Rua B"
    assert engenheiro_valido.endereco.numero == "230"
    assert engenheiro_valido.endereco.complemento == "Nada"
    assert engenheiro_valido.endereco.cep == "12839123"
    assert engenheiro_valido.endereco.cidade == "São Paulo"
    assert engenheiro_valido.endereco.uf == "São Paulo"
    assert engenheiro_valido.sexo == "FEMININO"
    assert engenheiro_valido.estadoCivil == "CASADO"
    assert engenheiro_valido.dataNascimento == "10/01/1980"
    assert engenheiro_valido.cpf == "01923102310"
    assert engenheiro_valido.rg == "237189201"
    assert engenheiro_valido.matricula == "3001"
    assert engenheiro_valido.setor == "ENGENHARIA"
    assert engenheiro_valido.salario == 8950.70
    assert engenheiro_valido.crea == "Crea-BA"
    
def test_engenheiro_crea_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O crea deve ser preenchido em texto."):
        Engenheiro(231,"Marta","71982718293","marta@gmail.com",Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","01923102310","237189201","3001",Setor.ENGENHARIA.name,8950.70,123)
    
def test_engenheiro_vazio_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O crea não pode ficar vazio"):
        return Engenheiro(231,"Marta","71982718293","marta@gmail.com",Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","01923102310","237189201","3001",Setor.ENGENHARIA.name,8950.70," ")