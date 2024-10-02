from validacao_dados.models.engenheiro import Engenheiro
from validacao_dados.models.endereco import Endereco
from validacao_dados.models.enums.estado_civil import EstadoCivil
from validacao_dados.models.enums.sexo import Sexo
from validacao_dados.models.enums.setor import Setor
from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa

import pytest

@pytest.fixture
def engenheiro_valido():
    return Engenheiro(231,"Marta","71982718293","marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","19231023100","237189201","3001",
                             Setor.ENGENHARIA.name,8950.70,"Crea-BA")

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
    assert engenheiro_valido.cpf == "19231023100"
    assert engenheiro_valido.rg == "237189201"
    assert engenheiro_valido.matricula == "3001"
    assert engenheiro_valido.setor == "ENGENHARIA"
    assert engenheiro_valido.salario == 8950.70
    assert engenheiro_valido.crea == "Crea-BA"


def test_enum_sexo_validos():
    Sexo.MASCULINO.name == "Masculino"
    Sexo.FEMININO.name == "FEMININO"
    
def test_enum_estadoCivil_validos():
    EstadoCivil.SOLTEIRO.name == "Solteiro"
    EstadoCivil.CASADO.name == "CASADO"
    EstadoCivil.SEPARADO.name == "SEPARADO"
    EstadoCivil.VIUVO.name == "VIUVO"
    EstadoCivil.DIVORCIO.name == "Divorciado"

def test_enums_setor_validos():
    Setor.ENGENHARIA.name == "Engenharia"
    Setor.JURIDICO.name == "Juridico"
    Setor.SAUDE.name == "Saude"

def test_pessoa_id_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O id deve ser em numeros inteiros"):
        Engenheiro("231","Marta","71982718293","marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","19231023100","237189201","3001",
                             Setor.ENGENHARIA.name,8950.70,"Crea-BA")

        
def test_pessoa_id_tipo_numero_negativo_retorna_mensagem():
    with pytest.raises(ValueError, match="O id não pode ser negativo"):
         Engenheiro(-231,"Marta","71982718293","marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","19231023100","237189201","3001",
                             Setor.ENGENHARIA.name,8950.70,"Crea-BA")


def test_pessoa_nome_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O nome deve ser em texto"):
         Engenheiro(231,7,"71982718293","marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","19231023100","237189201","3001",
                             Setor.ENGENHARIA.name,8950.70,"Crea-BA")


def test_pessoa_nome_tipo_vazio_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O nome não pode esta vazio"):
         Engenheiro(231," ","71982718293","marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","19231023100","237189201","3001",
                             Setor.ENGENHARIA.name,8950.70,"Crea-BA")
        
def test_pessoa_nome_tipo_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="Digite um nome com no minimo 3 letras"):
         Engenheiro(231,"Ma","71982718293","marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","19231023100","237189201","3001",
                             Setor.ENGENHARIA.name,8950.70,"Crea-BA")
        
def test_pessoa_telefone_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O telefone deve ser em texto"):
        Engenheiro(231,"Marta",71982718293,"marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","19231023100","237189201","3001",
                             Setor.ENGENHARIA.name,8950.70,"Crea-BA")

def test_pessoa_telefone_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="Digite o número com 11 digitos, incluindo o dd"):
        Engenheiro(231,"Marta","7198271","marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","19231023100","237189201","3001",
                             Setor.ENGENHARIA.name,8950.70,"Crea-BA")

        
def test_pessoa_email_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O email deve ser em texto"):
         Engenheiro(231,"Marta","71982718293",710,
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","19231023100","237189201","3001",
                             Setor.ENGENHARIA.name,8950.70,"Crea-BA")

def test_pessoa_email_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O email deve ter no minino 15 digitos"):
            Engenheiro(231,"Marta","71982718293","mar@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","19231023100","237189201","3001",
                             Setor.ENGENHARIA.name,8950.70,"Crea-BA")


def test_fisica_dataNascimento_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="A data nascimento deve ser em texto"):
          Engenheiro(231,"Marta","71982718293","marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,10011980,"19231023100","237189201","3001",
                             Setor.ENGENHARIA.name,8950.70,"Crea-BA")

        
def test_fisica_dataNascimento_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="A data de nascimento deve conter 10 digitos junto com '/'"):
         Engenheiro(231,"Marta","71982718293","marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10011980","19231023100","237189201","3001",
                             Setor.ENGENHARIA.name,8950.70,"Crea-BA")

def test_funcionario_cpf_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O cpf deve ser preenchido em texto."):
         Engenheiro(231,"Marta","71982718293","marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980",19231023100,"237189201","3001",
                             Setor.ENGENHARIA.name,8950.70,"Crea-BA")

def test_funcionario_cpf_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O cpf deve ter 11 digitos"):
         Engenheiro(231,"Marta","71982718293","marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","192310231","237189201","3001",
                             Setor.ENGENHARIA.name,8950.70,"Crea-BA")

        
def test_funcionario_rg_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O rg deve ser preenchido em texto"):
         Engenheiro(231,"Marta","71982718293","marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","19231023100",237189201,"3001",
                             Setor.ENGENHARIA.name,8950.70,"Crea-BA")

def test_funcionario_rg_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O rg deve conter 9 digitos"):
        Engenheiro(231,"Marta","71982718293","marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","19231023100","2371892","3001",
                             Setor.ENGENHARIA.name,8950.70,"Crea-BA")

def test_funcionario_matricula_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="A matricula deve ser preenchida em texto"):
        Engenheiro(231,"Marta","71982718293","marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","19231023100","237189201",3001,
                             Setor.ENGENHARIA.name,8950.70,"Crea-BA")

def test_funcionario_matricula_vazio_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="A matricula não pode ficar vazia."):
          Engenheiro(231,"Marta","71982718293","marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","19231023100","237189201"," ",
                             Setor.ENGENHARIA.name,8950.70,"Crea-BA")

def test_funcionario_salario_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O salario deve ser inserido com numero com ponto flutuante"):
        Engenheiro(231,"Marta","71982718293","marta@gmail.com",
                Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                    Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","19231023100","237189201","3001",
                        Setor.ENGENHARIA.name,"8950.70","Crea-BA")

        
def test_funcionario_salario_negativo_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O salario não pode ser em números negativos"):
        Engenheiro(231,"Marta","71982718293","marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","19231023100","237189201","3001",
                             Setor.ENGENHARIA.name,-8950.70,"Crea-BA")

def test_engenheiro_crea_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O crea deve ser preenchido em texto."):
        Engenheiro(231,"Marta","71982718293","marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","19231023100","237189201","3001",
                             Setor.ENGENHARIA.name,8950.70,524)
def test_engenheiro_vazio_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O crea não pode ficar vazio"):
       Engenheiro(231,"Marta","71982718293","marta@gmail.com",
                      Endereco("Rua B","230","Nada","12839123","São Paulo",UnidadeFederativa.SAO_PAULO.nome),
                        Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/01/1980","19231023100","237189201","3001",
                             Setor.ENGENHARIA.name,8950.70," ")