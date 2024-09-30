from validacao_dados.models.enums.unidade_federativa import UnidadeFederativa

class Endereco:
    def __init__(self,logradouro: str,numero: str,complemento: str,cep: str,cidade: str,uf: UnidadeFederativa) -> None:
        self.logradouro = self._verificar_logradouro(logradouro)
        self.numero = self._verificar_numero(numero)
        self.complemento = self._verificar_complemento(complemento)
        self.cep = self._verificar_cep(cep)
        self.cidade = self._verificar_cidade(cidade)
        self.uf = uf
        
    def _verificar_logradouro(self,nome):
        self.__verificar_logradouro_tipo_invalido(nome)
        self.__verificar_logradouro_vazio_invalido(nome)
                
        self.logradouro = nome
        return self.logradouro
    
    def _verificar_numero(self,nome):
        self.__verificar_numero_tipo_invalido(nome)
        
        self.numero = nome
        return self.numero
    
    def _verificar_complemento(self,nome):
        self.__verificar_complemento_tipo_invalido(nome)
        
        self.complemento = nome
        return self.complemento
    
    def _verificar_cep(self,nome):
        self.__verificar_cep_tipo_invalido(nome)
        self.__verificar_cep_tamanho_invalido(nome)
        
        self.cep = nome
        return self.cep
    
    def _verificar_cidade(self,nome):
        self.__verificar_cidade_tipo_invalido(nome)
        self.__verificar_cidade_tamanho_invalido(nome)
        
        self.cidade = nome
        return self.cidade
    
    def __verificar_logradouro_tipo_invalido(self,nome):
        if not isinstance(nome, str):
            raise TypeError("O logradouro deve ser preenchido em texto.")
    
    def __verificar_logradouro_vazio_invalido(self,nome):
        if not nome.strip():
            raise TypeError("O Logradouro Não pode esta vazio")
    
    def __verificar_numero_tipo_invalido(self,nome):
        if not isinstance(nome,str):
            raise TypeError("O número deve ser preenchido em texto.")
        
    def __verificar_complemento_tipo_invalido(self,nome):
        if not isinstance(nome,str):
            raise TypeError("O Complemento deve ser preenchido em texto.")
        
    def __verificar_cep_tipo_invalido(self,nome):
        if not isinstance(nome,str):
            raise TypeError("O cep deve ser preenchido em texto.")
        
    def __verificar_cep_tamanho_invalido(self,nome):
        if len(nome) != 8:
            raise ValueError("Cep invalido, Por favor digitar oito algarismo")
        
    def __verificar_cidade_tipo_invalido(self,nome):
        if not isinstance(nome,str):
            raise TypeError("A cidade deve ser preenchida em texto")
    
    def __verificar_cidade_tamanho_invalido(self,nome):
        if len(nome) < 3:
            raise ValueError("Cidade Invalida, Por favor digite uma cidade valida")