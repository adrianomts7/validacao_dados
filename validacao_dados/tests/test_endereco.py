import pytest
from validacao_dados.models.endereco import Endereco
from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def endereco_valido():
    return Endereco("Rua A","22","Nada","12345678","Salvador",UnidadeFederativa.BAHIA.name)

def test_endereco_logradouro_valido(endereco_valido):
    assert endereco_valido.logradouro == "Rua A"
    
def test_endereco_numero_valido(endereco_valido):
    assert endereco_valido.numero == "22"
    
def test_endereco_complemento_valido(endereco_valido):
    assert endereco_valido.complemento == "Nada"
    
def test_endereco_cep_valido(endereco_valido):
    assert endereco_valido.cep == "12345678"

def test_endereco_cidade_valida(endereco_valido):
    assert endereco_valido.cidade == "Salvador"

def test_endereco_unidadeFedarativa_valido(endereco_valido):
    assert endereco_valido.uf == "BAHIA"

def test_enums_ufs_nomes_validos():
    assert UnidadeFederativa.BAHIA.nome == "Bahia"
    assert UnidadeFederativa.RIO_DE_JANEIRO.nome == "Rio de Janeiro"
    assert UnidadeFederativa.SAO_PAULO.nome == "São Paulo"

def test_enums_ufs_sigla_validos():
    assert UnidadeFederativa.BAHIA.sigla == "BA"
    assert UnidadeFederativa.RIO_DE_JANEIRO.sigla == "RJ"
    assert UnidadeFederativa.SAO_PAULO.sigla == "SP"

def test_endereco_logradouro_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O logradouro deve ser preenchido em texto."):
        Endereco(22,"22","Nada","123","Salvador",UnidadeFederativa.BAHIA.nome)

def test_endereco_logradouro_vazio():
    with pytest.raises(TypeError, match="O Logradouro Não pode esta vazio"):
        Endereco("","22","Nada","123","Salvador",UnidadeFederativa.BAHIA.nome)
        
def test_endereco_numero_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O número deve ser preenchido em texto."):
        Endereco("Rua A",22,"Nada","9879","Salvador",UnidadeFederativa.BAHIA.nome)
        
def test_endereco_complemento_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match=" Complemento deve ser preenchido em texto."):
        Endereco("Rua A","22",123,"9879","Salvador",UnidadeFederativa.BAHIA.nome)
        
def test_endereco_cep_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O cep deve ser preenchido em texto."):
        Endereco("Rua A","22","nada",9879,"Salvador",UnidadeFederativa.BAHIA.nome)
        
def test_endereco_cep_tamanho_invalido():
    with pytest.raises(ValueError, match="Cep invalido, Por favor digitar oito algarismo"):
        Endereco("Rua A","22","nada","123456","Salvador",UnidadeFederativa.BAHIA.nome)
        
def test_endereco_cidade_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="A cidade deve ser preenchida em texto"):
        Endereco("Rua A","22","nada","12345679",22,UnidadeFederativa.BAHIA.nome)
        
def test_endereco_cidade_tamanho_invalido():
    with pytest.raises(ValueError, match="Cidade Invalida, Por favor digite uma cidade valida"):
        Endereco("Rua A","22","nada","12345679","AB",UnidadeFederativa.BAHIA.nome)