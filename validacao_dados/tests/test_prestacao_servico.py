from validacao_dados.models.prestacao_servico import PrestacaoServico
from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa
from validacao_dados.models.endereco import Endereco

import pytest

@pytest.fixture
def prestacaoServico_valido():
    return PrestacaoServico(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),"18793871812","123456789","28/09/2024","29/10/2024")
    
def test_prestacaoServico_contratoInicio_valido(prestacaoServico_valido):
   assert prestacaoServico_valido.contratoInicio == "28/09/2024"

def test_prestacaoServico_contratoFim_valido(prestacaoServico_valido):
    assert prestacaoServico_valido.contratoFim == "29/10/2024"
    
def test_prestacaoServico_contratoInicio_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O inicio do Contrato deve ser em texto"):
        PrestacaoServico(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),"18793871812","123456789",28092024,"29/10/2024")
        
def test_prestacaoServico_contratoInicio_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O inicio do contrato deve conter no minimo 10 Digitos da data junto com '/' " ):
        PrestacaoServico(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),"18793871812","123456789","28/9/2024","29/10/2024")
        
def test_pretacaoServico_contratoFim_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O final do contrato deve ser em texto"):
        PrestacaoServico(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),"18793871812","123456789","28/09/2024",2912024)
        
def test_prestacaoServico_contratoFim_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O fim do contrato deve conter no minino 10 Digitos da data junto com '/'"):
        PrestacaoServico(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),"18793871812","123456789","28/09/2024","29/1/2024")