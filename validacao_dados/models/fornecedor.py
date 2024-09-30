from validacao_dados.models.endereco import Endereco
from validacao_dados.models.juridica import Juridica

class Fornecedor(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str,produto: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.produto = self._verificar_produto(produto)
    
    def _verificar_produto(self,valor):
        self.__verificar_produto_tipo_invalido(valor)
        self.__verificar_produto_tamanho_invalido(valor)
        
        self.produto = valor
        return self.produto
    
    def __verificar_produto_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O produto tem que ser em texto")
        
    def __verificar_produto_tamanho_invalido(self,valor):
        if len(valor) < 3:
            raise ValueError("O produto tem que ter mais do que 3 letras")
    