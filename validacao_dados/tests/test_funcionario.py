from validacao_dados.models.funcionario import Funcionario
from validacao_dados.models.endereco import Endereco
from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa
from validacao_dados.models.enums.sexo import Sexo
from validacao_dados.models.enums.estado_civil import EstadoCivil
from validacao_dados.models.enums.setor import Setor

import pytest

@pytest.fixture
def funcionario_valido():
    return Funcionario(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999","12345123514","231234592","20",Setor.ENGENHARIA,5000.99)

def test_funcionario_cpf_valido(funcionario_valido):
    assert funcionario_valido.cpf == "12345123514"
    
def test_funcionario_rg_valido(funcionario_valido):
    assert funcionario_valido.rg == "231234592"

def test_funcionario_matricula_valida(funcionario_valido):
    assert funcionario_valido.matricula == "20"
    
def test_funcionario_salrio_valido(funcionario_valido):
    assert funcionario_valido.salario == 5000.99   
    

def test_enums_setor_validos():
    Setor.ENGENHARIA.name == "Engenharia"
    Setor.JURIDICO.name == "Juridico"
    Setor.SAUDE.name == "Saude"
    
def test_funcionario_cpf_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O cpf deve ser preenchido em texto."):
        Funcionario(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999",12345123514,"231234592","20",Setor.ENGENHARIA,5000.99)
        
def test_funcionario_cpf_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O cpf deve ter 11 digitos"):
        Funcionario(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999","123451235","231234592","20",Setor.ENGENHARIA,5000.99)
        
def test_funcionario_rg_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O rg deve ser preenchido em texto"):
        Funcionario(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999","12345123514",231234592,"20",Setor.ENGENHARIA,5000.99)
        
def test_funcionario_rg_tamanho_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O rg deve conter 9 digitos"):
        Funcionario(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999","12345123514","2312345","20",Setor.ENGENHARIA,5000.99)
        
def test_funcionario_matricula_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="A matricula deve ser preenchida em texto"):
        Funcionario(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999","12345123514","231234592",20,Setor.ENGENHARIA,5000.99)
        
def test_funcionario_matricula_vazio_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="A matricula não pode ficar vazia."):
         Funcionario(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999","12345123514","231234592","",Setor.ENGENHARIA,5000.99)
         
def test_funcionario_salario_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O salario deve ser inserido com numero com ponto flutuante"):
        Funcionario(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999","12345123514","231234592","20",Setor.ENGENHARIA,"5000.99")
        
def test_funcionario_salario_negativo_invalido_retorna_mensagem():
    with pytest.raises(ValueError, match="O salario não pode ser em números negativos"):
        Funcionario(12345,"Adriano","71976516212","adriano@gmail.com", Endereco("Rua A","20","Nada","71622817","Salvador",UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.name,EstadoCivil.SOLTEIRO,"20/10/1999","12345123514","231234592","20",Setor.ENGENHARIA,-5000.99)