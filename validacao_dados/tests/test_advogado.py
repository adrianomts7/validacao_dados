from validacao_dados.models.advogado import Advogado
from validacao_dados.models.endereco import Endereco
from validacao_dados.models.enums.estado_civil import EstadoCivil
from validacao_dados.models.enums.sexo import Sexo
from validacao_dados.models.enums.setor import Setor
from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa

import pytest

@pytest.fixture
def advogado_valido():
    return Advogado(879,"Marivalda","71982736101","marivalda@gmail.com",
                    Endereco("Rua B","90","Nada","71829123","Salvador",
                             UnidadeFederativa.BAHIA.name),Sexo.FEMININO.name,
                             EstadoCivil.CASADO.name,"10/04/1990","18293019231","910297361","8871",
                             Setor.JURIDICO.name,7580.00,"Criminalista")

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
         Advogado("12345","Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)
        
def test_pessoa_id_tipo_numero_negativo_retorna_mensagem():
    with pytest.raises(ValueError, match="O id não pode ser negativo"):
         Advogado(-12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)

def test_pessoa_nome_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O nome deve ser em texto"):
         Advogado(12345,889,"71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)

def test_pessoa_nome_tipo_vazio_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O nome não pode esta vazio"):
         Advogado(12345," ","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)
        
def test_pessoa_nome_tipo_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="Digite um nome com no minimo 3 letras"):
         Advogado(12345,"AB","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)
        
def test_pessoa_telefone_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O telefone deve ser em texto"):
         Advogado(12345,"Adriano",71976516123,"adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)
        
def test_pessoa_telefone_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="Digite o número com 11 digitos, incluindo o dd"):
        Advogado(12345,"Adriano","719765","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)
        
def test_pessoa_email_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O email deve ser em texto"):
         Advogado(12345,"Adriano","71976509871",123098, Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)
        
def test_pessoa_email_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O email deve ter no minino 15 digitos"):
            Advogado(12345,"Adriano","71976509871","ano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",1234567891011)

def test_fisica_dataNascimento_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="A data nascimento deve ser em texto"):
          Advogado(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,20101999,1234567891011)
        
def test_fisica_dataNascimento_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="A data de nascimento deve conter 10 digitos junto com '/'"):
         Advogado(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20101999",1234567891011)

def test_funcionario_cpf_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O cpf deve ser preenchido em texto."):
         Advogado(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",12345123514,"231234592","20",Setor.ENGENHARIA,5000.99)
        
def test_funcionario_cpf_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O cpf deve ter 11 digitos"):
         Advogado(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999","123451235","231234592","20",Setor.ENGENHARIA,5000.99)
        
def test_funcionario_rg_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O rg deve ser preenchido em texto"):
         Advogado(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999","12345123514",231234592,"20",Setor.ENGENHARIA,5000.99)
        
def test_funcionario_rg_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O rg deve conter 9 digitos"):
         Advogado(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999","12345123514","2312345","20",Setor.ENGENHARIA,5000.99)
        
def test_funcionario_matricula_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="A matricula deve ser preenchida em texto"):
         Advogado(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999","12345123514","231234592",20,Setor.ENGENHARIA,5000.99)
        
def test_funcionario_matricula_vazio_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="A matricula não pode ficar vazia."):
          Advogado(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999","12345123514","231234592","",Setor.ENGENHARIA,5000.99)
         
def test_funcionario_salario_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O salario deve ser inserido com numero com ponto flutuante"):
         Advogado(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999","12345123514","231234592","20",Setor.ENGENHARIA,"5000.99")
        
def test_funcionario_salario_negativo_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O salario não pode ser em números negativos"):
         Advogado(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999","12345123514","231234592","20",Setor.ENGENHARIA,-5000.99)

def test_advogado_oab_tipo_invalida_retorna_mensagem():
    with pytest.raises(TypeError, match="A oab deve ser preenchida em texto."):
        Advogado(879,"Marivalda","71982736101","marivalda@gmail.com",Endereco("Rua B","90","Nada","71829123","Salvador",UnidadeFederativa.BAHIA.name),Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/04/1990","18293019231","910297361","8871",Setor.JURIDICO.name,7580.00,71)
        
def test_advogado_oab_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="A oab não pode ficar vazio"):
        Advogado(879,"Marivalda","71982736101","marivalda@gmail.com",Endereco("Rua B","90","Nada","71829123","Salvador",UnidadeFederativa.BAHIA.name),Sexo.FEMININO.name,EstadoCivil.CASADO.name,"10/04/1990","18293019231","910297361","8871",Setor.JURIDICO.name,7580.00," ")
    
