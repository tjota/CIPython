class Car():
    """Uma tentativa simples de representar um carro."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """Devolve um nome descritivo, formatado de modo elegante"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


    def update_odometer(self, mileage):
        """Define o valor de leitura do hodômetro com o valor especificado."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, miles):
        """Soma a quantidade especificada ao valor do hodômetro."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")


    def fill_gas_tank():
        """Carros normais possuem tanques de gasolina."""
        print("This car needs a gas tank!")


class Battery():
    """Uma tentativa simples de modelar uma bateria para um carro elétrico"""

    def __init__(self, battery_size=70):
        """Inicializa os atributos da bateria."""
        self.battery_size = battery_size


    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


    def get_range(self):
        """Exibe uma frase sobre a distância que o carro é capaz de percorrer
        com essa bateria."""
        if self.battery_size == 70:
            rangee = 240
        elif self.battery_size == 85:
            rangee = 270

        message = "This car can go approximately " + str(rangee)
        message += " miles on a full charge."
        print(message)


    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85



class ElectricCar(Car):
    """Representa aspectos de um carro específico."""

    def __init__(self, make, model, year):
        """Inicializa os atributos da class-pai."""
        super().__init__(make, model, year)
        self.battery = Battery()


    def fill_gas_tank():
        """Carros elétricos não têm tanques de gasolina."""
        print("This car doesn't need a gas tank!")


my_eletric_car = ElectricCar('Suzuki', 'Jimmy', '2018')
my_eletric_car.battery.get_range()

my_eletric_car.battery.upgrade_battery()
my_eletric_car.battery.get_range()