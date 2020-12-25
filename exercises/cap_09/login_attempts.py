class User:

    def __init__(self, first_name, last_name, cpf, rg, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.rg = rg
        self.login_attempts = login_attempts

    
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


    def increment_login_attempts(self, attempt=1):
        self.login_attempts += attempt


    def reset_login_attempts(self):
        self.login_attempts = 0

atrib_user = ['Thiago', 'Jack', '56432', '894394']

user = User('Thiago', 'Jack', '56432', '894394')
user.increment_login_attempts()
print(user.login_attempts)

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)

user.reset_login_attempts()
print(user.login_attempts)


"""
user_0 = User('Thiago', 'Jack', '848484', '938383')
user_0.describe_user()
user_0.greet_user()

user_1 = User('Thayse', 'Lobato', '876754', '97673')
user_1.describe_user()
user_1.greet_user()

user_2 = User('Clarice', 'Lobato', '834534', '935543')
user_2.describe_user()
user_2.greet_user()
"""