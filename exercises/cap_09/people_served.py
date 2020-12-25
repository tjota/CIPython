class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served


    def describe_restaurant(self):
        print(self.restaurant_name + " " + self.cuisine_type)
        print(str(self.number_served) + " pessoas atendidas até o momento.")


    def open_restaurant(self):
        print("\nAbrindo restaurante...")
        print("Restaurante aberto.\n")

    
    def set_number_served(self, num_served):
        self.number_served = num_served

    
    def increment_number_served(self, plus_served):
        self.number_served += plus_served


restaurant = Restaurant('Sabor da Bahia', 'Comida Baiana')
restaurant.describe_restaurant()
restaurant.set_number_served(18)
restaurant.describe_restaurant()

restaurant.increment_number_served(13)
restaurant.describe_restaurant()