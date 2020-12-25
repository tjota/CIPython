class Pessoa:
    """Classe genérica para um entidade Pessoa."""

    def __init__(self, nome, endereco, cpf, rg):
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf
        self.rg = rg


    def mostra_info_completa(self):
        pessoa = {
            'Nome': self.nome,
            'Endereço': self.endereco,
            'CPF': self.cpf,
            'RG': self.rg,
            }

        for item, atributo in pessoa.items():
            print(item + ": " + atributo)

class Cliente(Pessoa):
    """Define a estrutura de um cliente."""

    def __init__(self, nome, endereco, cpf, rg, limite):
        """Inicializa a classe-pai."""
        super().__init__(nome, endereco, cpf, rg)
        self.limite = limite


class Colaborador(Pessoa):
    """Define o que é um colaborador."""

    def __init__(self, nome, endereco, cpf, rg, setor, salario):
        super().__init__(nome, endereco, cpf, rg)
        self.setor = setor
        self.salario = salario


#pessoa = Pessoa('Thiago Jack', 'Av Art', '068354', '20819')
#pessoa.mostra_info_completa()

cliente = Cliente('Thayse Lobato', 'Av Art', '098723', '345632', 100)
cliente.mostra_info_completa()