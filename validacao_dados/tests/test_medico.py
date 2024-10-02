from validacao_dados.models.medico import Medico
from validacao_dados.models.endereco import Endereco
from validacao_dados.models.enums.estado_civil import EstadoCivil
from validacao_dados.models.enums.sexo import Sexo
from validacao_dados.models.enums.setor import Setor
from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa

import pytest

@pytest.fixture
def medico_valido():
    return Medico(476,"Mateus","71916271029","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239","8719",
                        Setor.SAUDE.name,10550.80,"Cirugião")

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
       Medico("476","Mateus","71916271029","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239","8719",
                        Setor.SAUDE.name,10550.80,"Cirugião")

        
def test_pessoa_id_tipo_numero_negativo_retorna_mensagem():
    with pytest.raises(ValueError, match="O id não pode ser negativo"):
         Medico(-476,"Mateus","71916271029","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239","8719",
                        Setor.SAUDE.name,10550.80,"Cirugião")


def test_pessoa_nome_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O nome deve ser em texto"):
         Medico(476,22,"71916271029","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239","8719",
                        Setor.SAUDE.name,10550.80,"Cirugião")


def test_pessoa_nome_tipo_vazio_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O nome não pode esta vazio"):
         Medico(476," ","71916271029","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239","8719",
                        Setor.SAUDE.name,10550.80,"Cirugião")
        
def test_pessoa_nome_tipo_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="Digite um nome com no minimo 3 letras"):
         Medico(476,"Ma","71916271029","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239","8719",
                        Setor.SAUDE.name,10550.80,"Cirugião")
        
def test_pessoa_telefone_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O telefone deve ser em texto"):
        Medico(476,"Mateus",71916271029,"mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239","8719",
                        Setor.SAUDE.name,10550.80,"Cirugião")

def test_pessoa_telefone_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="Digite o número com 11 digitos, incluindo o dd"):
        Medico(476,"Mateus","71916271","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239","8719",
                        Setor.SAUDE.name,10550.80,"Cirugião")

        
def test_pessoa_email_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O email deve ser em texto"):
         Medico(476,"Mateus","71916271029",213,
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239","8719",
                        Setor.SAUDE.name,10550.80,"Cirugião")

def test_pessoa_email_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O email deve ter no minino 15 digitos"):
            Medico(476,"Mateus","71916271029","teu@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239","8719",
                        Setor.SAUDE.name,10550.80,"Cirugião")

def test_fisica_dataNascimento_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="A data nascimento deve ser em texto"):
          Medico(476,"Mateus","71916271029","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,30031970,"18920817231","823910239","8719",
                        Setor.SAUDE.name,10550.80,"Cirugião")

        
def test_fisica_dataNascimento_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="A data de nascimento deve conter 10 digitos junto com '/'"):
         Medico(476,"Mateus","71916271029","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30031970","18920817231","823910239","8719",
                        Setor.SAUDE.name,10550.80,"Cirugião")
         
def test_funcionario_cpf_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O cpf deve ser preenchido em texto."):
        Medico(476,"Mateus","71916271029","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970",18920817231,"823910239","8719",
                        Setor.SAUDE.name,10550.80,"Cirugião")

def test_funcionario_cpf_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O cpf deve ter 11 digitos"):
         Medico(476,"Mateus","71916271029","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817","823910239","8719",
                        Setor.SAUDE.name,10550.80,"Cirugião")

def test_funcionario_rg_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O rg deve ser preenchido em texto"):
         Medico(476,"Mateus","71916271029","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231",823910239,"8719",
                        Setor.SAUDE.name,10550.80,"Cirugião")

def test_funcionario_rg_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O rg deve conter 9 digitos"):
        Medico(476,"Mateus","71916271029","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","8239102","8719",
                        Setor.SAUDE.name,10550.80,"Cirugião")

def test_funcionario_matricula_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="A matricula deve ser preenchida em texto"):
        Medico(476,"Mateus","71916271029","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239",8719,
                        Setor.SAUDE.name,10550.80,"Cirugião")

def test_funcionario_matricula_vazio_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="A matricula não pode ficar vazia."):
          Medico(476,"Mateus","71916271029","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239"," ",
                        Setor.SAUDE.name,10550.80,"Cirugião")

def test_funcionario_salario_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O salario deve ser inserido com numero com ponto flutuante"):
        Medico(476,"Mateus","71916271029","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239","8719",
                        Setor.SAUDE.name,"10550.80","Cirugião")
        
def test_funcionario_salario_negativo_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O salario não pode ser em números negativos"):
        Medico(476,"Mateus","71916271029","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239","8719",
                        Setor.SAUDE.name,-10550.80,"Cirugião")

def test_medico_crm_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O crm deve ser preenchido em texto"):
       Medico(476,"Mateus","71916271029","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239","8719",
                        Setor.SAUDE.name,10550.80,8754)
       
def test_medico_crm_vazio_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O crm não pode esta vazio"):
        Medico(476,"Mateus","71916271029","mateus@gmail,com",
                  Endereco("Rua Carioca","022","Após a ponte rio-niteroi","22982981","Niteroi",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                    Sexo.MASCULINO.name,EstadoCivil.SEPARADO.name,"30/03/1970","18920817231","823910239","8719",
                        Setor.SAUDE.name,10550.80,"")