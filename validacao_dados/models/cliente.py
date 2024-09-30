from validacao_dados.models.endereco import Endereco
from validacao_dados.models.enums.estado_civil import EstadoCivil
from validacao_dados.models.enums.sexo import Sexo
from validacao_dados.models.fisica import Fisica

class Cliente(Fisica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str,protocoloAtendimento: int) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.protocoloAtendimento = self._verificar_protocoloAtendimento(protocoloAtendimento)
        
    def _verificar_protocoloAtendimento(self,valor):
        self.__vericar_protocoloAtendimento_tipo_invalido(valor)
        self.__verificar_protocoloAtendimento_numero_negativo_invalido(valor)
        
        self.protocoloAtendimento = valor
        return self.protocoloAtendimento
    
    def __vericar_protocoloAtendimento_tipo_invalido(self,valor):
        if not isinstance(valor, int):
            raise TypeError("O protocolo de atendimento deve ser preenchido em números inteiros")
        
    def __verificar_protocoloAtendimento_numero_negativo_invalido(self,valor):
        if valor < 0:
            raise ValueError("Não pode digitar números negativos no protocolo de atendimento")