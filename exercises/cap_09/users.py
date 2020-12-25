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

user_0 = User('Thiago', 'Jack', '848484', '938383')
user_0.describe_user()
user_0.greet_user()

user_1 = User('Thayse', 'Lobato', '876754', '97673')
user_1.describe_user()
user_1.greet_user()

user_2 = User('Clarice', 'Lobato', '834534', '935543')
user_2.describe_user()
user_2.greet_user()