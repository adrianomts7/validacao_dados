from abc import ABC
from validacao_dados.models.endereco import Endereco

class Pessoa(ABC):
    def __init__(self,id: int,nome: str,telefone: str,email: str,endereco: Endereco) -> None:
        self.id = self._verificar_id(id)
        self.nome = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email = self._verificar_email(email)
        self.endereco = endereco
            
    def _verificar_id(self,valor):
        self.__verificar_id_tipo_invalido(valor)
        self.__verificar_id_numero_negativo(valor)
        
        self.id = valor
        return self.id
    
    def _verificar_nome(self,valor):
        self.__verificar_nome_tipo_invalido(valor)
        self.__verificar_nome_tipo_vazio_invalido(valor)
        self.__verificar_nome_tamanho_invalido(valor)
        
        self.nome = valor
        return self.nome
    
    def _verificar_telefone(self,valor):
        self.__verificar_telefone_tipo_invalido(valor)
        self.__verificar_telefone_tamanho_invalido(valor)
        
        self.telefone = valor
        return self.telefone
    
    def _verificar_email(self,valor):
        self.__verificar_email_tipo_invalido(valor)
        self.__verificar_email_tamanho_invalido(valor)
        
        self.email = valor
        return self.email
    
    def __verificar_id_tipo_invalido(self,valor):
        if not isinstance(valor, int):
            raise TypeError("O id deve ser em numeros inteiros")
        
    def __verificar_id_numero_negativo(self,valor):
        if valor <= 0:
            raise ValueError("O id não pode ser negativo")
        
    def __verificar_nome_tipo_invalido(self,valor):
        if not isinstance(valor,str):
            raise TypeError("O nome deve ser em texto")
        
    def __verificar_nome_tipo_vazio_invalido(self,valor):
        if not valor.strip():
            raise ValueError("O nome não pode esta vazio")
    
    def __verificar_nome_tamanho_invalido(self,valor):
        if len(valor) < 3:
            raise ValueError("Digite um nome com no minimo 3 letras")
        
    def __verificar_telefone_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O telefone deve ser em texto")
        
    def __verificar_telefone_tamanho_invalido(self,valor):
        if len(valor) != 11:
            raise ValueError("Digite o número com 11 digitos, incluindo o dd")
    
    def __verificar_email_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O email deve ser em texto")
        
    def __verificar_email_tamanho_invalido(self,valor):
        if len(valor) < 15:
            raise ValueError("O email deve ter no minino 15 digitos")
    