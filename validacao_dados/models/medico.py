from validacao_dados.models.endereco import Endereco
from validacao_dados.models.enums.estado_civil import EstadoCivil
from validacao_dados.models.enums.setor import Setor
from validacao_dados.models.enums.sexo import Sexo
from validacao_dados.models.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float,crm: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento, cpf, rg, matricula, setor, salario)
        self.crm = self._verificar_crm(crm)
        
    def _verificar_crm(self,valor):
        self.__verificar_crm_tipo_invalido(valor)
        self.__verificar_crm_vazio_invalido(valor)
        
        self.crm = valor
        return self.crm
        
    def __verificar_crm_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O crm deve ser preenchido em texto")
        
    def __verificar_crm_vazio_invalido(self,valor):
        if not valor.strip():
            raise ValueError("O crm não pode esta vazio")