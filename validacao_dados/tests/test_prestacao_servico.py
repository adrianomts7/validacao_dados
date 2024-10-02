from validacao_dados.models.prestacao_servico import PrestacaoServico
from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa
from validacao_dados.models.endereco import Endereco

import pytest

@pytest.fixture
def prestacaoServico_valido():
    return PrestacaoServico(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),"18793871812","123456789","28/09/2024","29/10/2024")

def test_pessoa_id_valido(prestacaoServico_valido):
    assert prestacaoServico_valido.id == 1234

def test_pessoa_nome_valido(prestacaoServico_valido):
    assert prestacaoServico_valido.nome == "Adriano"
    
def test_pessoa_telefone_valido(prestacaoServico_valido):
    assert prestacaoServico_valido.telefone == "71917268176"
    
def test_pessoa_email_valido(prestacaoServico_valido):
    assert prestacaoServico_valido.email == "adriano@gmail.com"

def test_juridica_cnpj_valido(prestacaoServico_valido):
    assert prestacaoServico_valido.cnpj == "18793871812"
    
def test_juridica_incricao_estadual_valido(prestacaoServico_valido):
    assert prestacaoServico_valido.incricaoEstadual == "123456789"
    
def test_prestacaoServico_contratoInicio_valido(prestacaoServico_valido):
   assert prestacaoServico_valido.contratoInicio == "28/09/2024"

def test_prestacaoServico_contratoFim_valido(prestacaoServico_valido):
    assert prestacaoServico_valido.contratoFim == "29/10/2024"
    
def test_pessoa_id_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O id deve ser em numeros inteiros"):
        PrestacaoServico("12345","Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),"18793871812","123456789","28/09/2024","29/10/2024")
        
def test_pessoa_id_tipo_numero_negativo_retorna_mensagem():
    with pytest.raises(ValueError, match="O id não pode ser negativo"):
        PrestacaoServico(-12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),"18793871812","123456789","28/09/2024","29/10/2024")

def test_pessoa_nome_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O nome deve ser em texto"):
        PrestacaoServico(12345,889,"71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),"18793871812","123456789","28/09/2024","29/10/2024")

def test_pessoa_nome_tipo_vazio_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O nome não pode esta vazio"):
        PrestacaoServico(12345," ","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),"18793871812","123456789","28/09/2024","29/10/2024")
        
def test_pessoa_nome_tipo_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="Digite um nome com no minimo 3 letras"):
        PrestacaoServico(12345,"AB","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),"18793871812","123456789","28/09/2024","29/10/2024")
        
def test_pessoa_telefone_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O telefone deve ser em texto"):
        PrestacaoServico(12345,"Adriano",71976516123,"adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),"18793871812","123456789","28/09/2024","29/10/2024")
        
def test_pessoa_telefone_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="Digite o número com 11 digitos, incluindo o dd"):
        PrestacaoServico(12345,"Adriano","719765","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),"18793871812","123456789","28/09/2024","29/10/2024")
        
def test_pessoa_email_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O email deve ser em texto"):
        PrestacaoServico(12345,"Adriano","71976509871",123098, Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),"18793871812","123456789","28/09/2024","29/10/2024")
        
def test_pessoa_email_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O email deve ter no minino 15 digitos"):
         PrestacaoServico(12345,"Adriano","71976509871","ano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),"18793871812","123456789","28/09/2024","29/10/2024")

def test_juridica_cnpj_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O Cnpj deve ser em texto"):
        PrestacaoServico(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),18793871812,"123456789","28/09/2024","29/10/2024")
        
def test_juridica_cnpj_tamanho_invalida_retorna_mensagem():
    with pytest.raises(ValueError, match="O cnpj deve conter no minimo 9 digitos"):
        PrestacaoServico(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),"1879387","123456789","28/09/2024","29/10/2024")
        
def test_juridico_incricaoEstadual_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="A incrição estadual deve ser em texto"):
        PrestacaoServico(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),"187938789",123456789,"28/09/2024","29/10/2024")
        
def test_juridico_inscricaoEstadual_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="A inscrição estadual deve conter 9 digitos"):
        PrestacaoServico(1234,"Adriano","71917268176","adriano@gmail.com",Endereco("Rua A","20","Nada","19872982","Salvador", UnidadeFederativa),"187938789","1234567","28/09/2024","29/10/2024")

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