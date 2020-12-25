class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(self.restaurant_name + " " + self.cuisine_type)


    def open_restaurant(self):
        print("\nAbrindo restaurante...")
        print("Restaurante aberto.\n")

# Opção 1: Utiliza variáveis e lista para armazenar os atributos.
restaurant_1 = Restaurant('Sabor do Sul', 'Pizzaria')
restaurant_2 = Restaurant('Sabor da Bahia', 'Comida Baiana')
restaurant_3 = Restaurant('La Pasta', 'Massas')

restaurantes = [restaurant_1, restaurant_2, restaurant_3]

for restaurante in restaurantes:
    restaurante.describe_restaurant()

# Opção 2: Utiliza um dicionário para armazenar os atributos.
rests = {
        'Sabor do Sul': 'Pizzaria',
        'Sabor da Bahia': 'Comida Baiana',
        'La Pasta': 'Massas',
        }


for rest, rest_type in rests.items():
    restaurante = Restaurant(rest, rest_type)
    restaurante.describe_restaurant()
