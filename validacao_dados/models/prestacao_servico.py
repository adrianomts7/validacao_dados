from validacao_dados.models.endereco import Endereco
from validacao_dados.models.juridica import Juridica

class PrestacaoServico(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricao_estadual: str,contratoInicio: str,contratoFim: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricao_estadual)
        self.contratoInicio = self._verificar_contratoInicio(contratoInicio)
        self.contratoFim = self._verificar_contratoFim(contratoFim)
        
    def _verificar_contratoInicio(self,valor):
        self.__verificar_contratoInicio_tipo_invalido(valor)
        self.__verificar_contratoInicio_tamanho_invalido(valor)
        
        self.contratoInicio = valor
        return self.contratoInicio
    
    def _verificar_contratoFim(self,valor):
        self.__verificar_contratoFim_tipo_invalido(valor)
        self.__verifcar_contratoFim_tamanho_invalido(valor)

        
        self.contratoFim = valor
        return self.contratoFim
    
    def __verificar_contratoInicio_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O inicio do Contrato deve ser em texto")
        
    def __verificar_contratoInicio_tamanho_invalido(self,valor):
        if len(valor) < 10:
            raise ValueError("O inicio do contrato deve conter no minimo 10 Digitos da data junto com '/' ")
        
    def __verificar_contratoFim_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O final do contrato deve ser em texto")
        
    def __verifcar_contratoFim_tamanho_invalido(self,valor):
        if len(valor) < 10:
            raise ValueError("O fim do contrato deve conter no minino 10 Digitos da data junto com '/' ")
        