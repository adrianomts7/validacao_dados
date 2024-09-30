from validacao_dados.models.endereco import Endereco
from validacao_dados.models.pessoa import Pessoa
from validacao_dados.models.enums.sexo import Sexo
from validacao_dados.models.enums.estado_civil import EstadoCivil

from abc import ABC

class Fisica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco,sexo: Sexo,estadoCivil: EstadoCivil,dataNascimento: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.dataNascimento = self._verificar_dataNascimento(dataNascimento)
        
    def _verificar_dataNascimento(self,valor):
        self.__verificar_dataNascimento_tipo_invalido(valor)
        self.__verificar_dataNascimento_tamanho_invalido(valor)
        
        self.dataNascimento = valor
        return self.dataNascimento
    
    def __verificar_dataNascimento_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("A data nascimento deve ser em texto")
        
    def __verificar_dataNascimento_tamanho_invalido(self,valor):
        if len(valor) != 10:
            raise ValueError("A data de nascimento deve conter 10 digitos junto com '/' ")
    