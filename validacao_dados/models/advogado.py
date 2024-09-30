from validacao_dados.models.endereco import Endereco
from validacao_dados.models.enums.estado_civil import EstadoCivil
from validacao_dados.models.enums.setor import Setor
from validacao_dados.models.enums.sexo import Sexo
from validacao_dados.models.funcionario import Funcionario

class Advogado(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float,oab: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento, cpf, rg, matricula, setor, salario)
        self.oab = self._verificar_oab(oab)
        
    def _verificar_oab(self,valor):
        self.__verificar_oab_tipo_invalido(valor)
        self.__verificar_oab_vazio_invalido(valor)
        
        self.oab = valor
        return self.oab
        
    def __verificar_oab_tipo_invalido(self,valor):
        if not isinstance(valor,str):
            raise TypeError("A oab deve ser preenchida em texto.")
        
    def __verificar_oab_vazio_invalido(self,valor):
        if not valor.strip():
            raise ValueError("A oab não pode ficar vazio")