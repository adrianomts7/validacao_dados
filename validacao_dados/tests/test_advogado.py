from validacao_dados.models.advogado import Advogado
from validacao_dados.models.endereco import Endereco
from validacao_dados.models.enums.estado_civil import EstadoCivil
from validacao_dados.models.enums.sexo import Sexo
from validacao_dados.models.enums.setor import Setor
from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa

import pytest

@pytest.fixture
def advogado_valido():
    return Advogado(879,"Marivalda","71982736101","marivalda@gmail.com",Endereco("Rua B","90","Nada","71829123","Salvador",UnidadeFederativa.BAHIA.name),Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/04/1990","18293019231","910297361","8871",Setor.JURIDICO.name,7580.00,"Criminalista")

def test_advogado_valido(advogado_valido):
    assert advogado_valido.id == 879
    assert advogado_valido.nome == "Marivalda"
    assert advogado_valido.telefone == "71982736101"
    assert advogado_valido.email == "marivalda@gmail.com"
    assert advogado_valido.endereco.logradouro == "Rua B"
    assert advogado_valido.endereco.numero == "90"
    assert advogado_valido.endereco.complemento == "Nada"
    assert advogado_valido.endereco.cep == "71829123"
    assert advogado_valido.endereco.cidade == "Salvador"
    assert advogado_valido.endereco.uf == "BAHIA"
    assert advogado_valido.sexo == "FEMININO"
    assert advogado_valido.estadoCivil == "CASADO"
    assert advogado_valido.dataNascimento == "10/04/1990"
    assert advogado_valido.cpf == "18293019231"
    assert advogado_valido.rg == "910297361"
    assert advogado_valido.setor == "JURIDICO"
    assert advogado_valido.salario == 7580.00
    assert advogado_valido.oab == "Criminalista"
    
def test_advogado_oab_tipo_invalida_retorna_mensagem():
    with pytest.raises(TypeError, match="A oab deve ser preenchida em texto."):
        Advogado(879,"Marivalda","71982736101","marivalda@gmail.com",Endereco("Rua B","90","Nada","71829123","Salvador",UnidadeFederativa.BAHIA.name),Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/04/1990","18293019231","910297361","8871",Setor.JURIDICO.name,7580.00,71)
        
def test_advogado_oab_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="A oab não pode ficar vazio"):
        Advogado(879,"Marivalda","71982736101","marivalda@gmail.com",Endereco("Rua B","90","Nada","71829123","Salvador",UnidadeFederativa.BAHIA.name),Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/04/1990","18293019231","910297361","8871",Setor.JURIDICO.name,7580.00," ")
    
