class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(self.restaurant_name + " " + self.cuisine_type)


    def open_restaurant(self):
        print("\nAbrindo restaurante...")
        print("Restaurante aberto.\n")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['morango', 'uva', 'melância', 'abacaxi']


    def get_flavors(self):
        print("Temos os seguintes sabores no cardápio:")
        for flavor in self.flavors:
            print("- " + flavor.title())


sorveteria = IceCreamStand('Sorveteria do Jack', 'Sorvetes e doces')
sorveteria.get_flavors()
