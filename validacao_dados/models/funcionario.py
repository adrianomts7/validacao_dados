from validacao_dados.models.endereco import Endereco
from validacao_dados.models.enums.estado_civil import EstadoCivil
from validacao_dados.models.enums.sexo import Sexo
from validacao_dados.models.fisica import Fisica
from validacao_dados.models.enums.setor import Setor

from abc import ABC

class Funcionario(Fisica,ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str,cpf: str,rg: str,matricula: str,setor: Setor,salario: float) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.cpf = self._verificar_cpf(cpf)
        self.rg = self._verificar_rg(rg)
        self.matricula = self._verificar_matricula(matricula)
        self.setor = setor
        self.salario = self._verificar_salario(salario)
        
    def _verificar_cpf(self,valor):
        self.__verificar_cpf_tipo_invalido(valor)
        self.__verificar_cpf_tamanho_invalido(valor)
        
        self.cpf = valor
        return self.cpf
    
    def _verificar_rg(self,valor):
        self.__verificar_rg_tipo_invalido(valor)
        self.__verificar_rg_tamanho_invalido(valor)
        
        self.rg = valor
        return self.rg
    
    def _verificar_matricula(self,valor):
        self.__verificar_matricula_tipo_invalido(valor)
        self.__verificar_matricula_vazio_invalido(valor)
        
        self.matricula = valor
        return self.matricula
    
    def _verificar_salario(self,valor):
        self.__verificar_salario_tipo_invalido(valor)
        self.__verificar_salario_negativo(valor)
        
        self.salario = valor
        return self.salario   
        
    def __verificar_cpf_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O cpf deve ser preenchido em texto.")
        
    def __verificar_cpf_tamanho_invalido(self,valor):
        if len(valor) != 11:
            raise ValueError("O cpf deve ter 11 digitos")
        
    def __verificar_rg_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O rg deve ser preenchido em texto")
        
    def __verificar_rg_tamanho_invalido(self,valor):
        if len(valor) != 9:
            raise ValueError("O rg deve conter 9 digitos")
          
    def __verificar_matricula_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("A matricula deve ser preenchida em texto")
        
    def __verificar_matricula_vazio_invalido(self,valor):
        if not valor.strip():
            raise ValueError("A matricula não pode ficar vazia.")
        
    def __verificar_salario_tipo_invalido(self,valor):
        if not isinstance(valor, float):
            raise TypeError("O salario deve ser inserido com numero com ponto flutuante")
        
    def __verificar_salario_negativo(self,valor):
        if valor < 0:
            raise ValueError("O salario não pode ser em números negativos")
        