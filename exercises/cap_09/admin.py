class User:

    def __init__(self, first_name, last_name, cpf, rg):
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.rg = rg

    
    def describe_user(self):
        user_info = {
            'Nome': self.first_name,
            'Sobrenome': self.last_name,
            'CPF': self.cpf,
            'RG': self.rg,
            }

        for item, valor in user_info.items():
            print(item + ": " + valor)

    
    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        print("\nOlá " + full_name + ", seja bem vindo!")


class Admin(User):

    def __init__(self, first_name, last_name, cpf, rg):
        super().__init__(first_name, last_name, cpf, rg)
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can delete all']

    
    def show_privileges(self):
        print('Privilégios de Administrador:')
        for privilege in self.privileges:
            print("- " + privilege.title())


root = Admin('Thiago', 'Jack', '098765', '45678965')
root.show_privileges()