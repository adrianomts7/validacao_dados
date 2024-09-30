from validacao_dados.models.medico import Medico
from validacao_dados.models.endereco import Endereco
from validacao_dados.models.enums.estado_civil import EstadoCivil
from validacao_dados.models.enums.sexo import Sexo
from validacao_dados.models.enums.setor import Setor
from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa

import pytest

@pytest.fixture
def medico_valido():
    return Medico(476,"Mateus","71916271029","mateus@gmail,com",Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239","8719",Setor.SAUDE.name,10550.80,"Cirugião")

def test_medico_valido(medico_valido):
    assert medico_valido.id == 476
    assert medico_valido.nome == "Mateus"
    assert medico_valido.telefone == "71916271029"
    assert medico_valido.email == "mateus@gmail,com"
    assert medico_valido.endereco.logradouro == "Rua Carioca"
    assert medico_valido.endereco.numero == "022"
    assert medico_valido.endereco.complemento == "Após a ponte rio-niteroi"
    assert medico_valido.endereco.cep == "22982981"
    assert medico_valido.endereco.cidade == "Niteroi"
    assert medico_valido.endereco.uf == "Rio de Janeiro"
    assert medico_valido.sexo == "MASCULINO"
    assert medico_valido.estadoCivil == "SEPARADO"
    assert medico_valido.dataNascimento == "30/03/1970"
    assert medico_valido.cpf == "18920817231"
    assert medico_valido.rg == "823910239"
    assert medico_valido.matricula == "8719"
    assert medico_valido.setor == "SAUDE"
    assert medico_valido.salario == 10550.80
    assert medico_valido.crm == "Cirugião"
    
def test_medico_crm_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O crm deve ser preenchido em texto"):
        Medico(476,"Mateus","71916271029","mateus@gmail,com",Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239","8719",Setor.SAUDE.name,10550.80,22)
    
def test_medico_crm_vazio_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O crm não pode esta vazio"):
        Medico(476,"Mateus","71916271029","mateus@gmail,com",Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239","8719",Setor.SAUDE.name,10550.80," ")
    