from validacao_dados.models.pessoa import Pessoa
from validacao_dados.models.endereco import Endereco
from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa

from abc import ABC

class Juridica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco,cnpj: str,inscricaoEstadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = self._verificar_cnpj(cnpj)
        self.incricaoEstadual = self._verificar_incricaoEstadual(inscricaoEstadual)
        
        
    def _verificar_cnpj(self,valor):
        self.__verificar_cnpj_tipo_invalido(valor)
        self.__verificar_cnpj_tamanho_invalido(valor)
        
        self.cnpj = valor
        return self.cnpj
    
    def _verificar_incricaoEstadual(self,valor):
        self.__verifcar_incricao_tipo_invalido(valor)
        self.__verificar_incricao_tamanho_invalido(valor)
        
        self.incricaoEstadual = valor
        return self.incricaoEstadual
    
    def __verificar_cnpj_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O Cnpj deve ser em texto")
        
    def __verificar_cnpj_tamanho_invalido(self,valor):
        if len(valor) < 9:
            raise ValueError("O cnpj deve conter no minimo 9 digitos")
        
    def __verifcar_incricao_tipo_invalido(self,valor):
        if not isinstance(valor,str):
            raise TypeError("A incrição estadual deve ser em texto")
        
    def __verificar_incricao_tamanho_invalido(self,valor):
        if len(valor) != 9:
            raise ValueError("A inscrição estadual deve conter 9 digitos")
        
    