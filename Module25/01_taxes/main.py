class Property:
    def __init__(self, worth):
        self.worth = worth

    def calculate_tax(self):
        pass


class Apartment(Property):
    def __init__(self, worth, address):
        super().__init__(worth)
        self.address = address

    def calculate_tax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth, model):
        super().__init__(worth)
        self.model = model

    def calculate_tax(self):
        return self.worth / 200


class CountyHouse(Property):
    def __init__(self, worth, address):
        super().__init__(worth)
        self.address = address

    def calculate_tax(self):
        return self.worth / 500


if __name__ == '__main__':
    total_many = int(input('Сколько у вас денег? '))
    apartment_price = int(input('Сколько стоит ваша квартира? '))
    car_price = int(input('Сколько стоит ваша машина? '))
    country_house_price = int(input('Сколько стоит ваша дача? '))

    apartment = Apartment(apartment_price, 'Lenin str. 100 1')
    car = Car(car_price, 'Land-cruiser 200')
    country_house = CountyHouse(country_house_price, 'Marks str. 200')

    print()
    print(f'Налог на квартиру по адресу: {apartment.address} - {apartment.calculate_tax()}')
    print(f'Налог на машину {car.model} - {car.calculate_tax()}')
    print(f'Налог на дачу по адресу: {country_house.address} - {car.calculate_tax()}')

    total_tax = apartment.calculate_tax() + car.calculate_tax() + car.calculate_tax()

    print('\nОбщий налог на имущество: ', total_tax)

    if total_tax > total_many:
        print('\nУ вас не хватает ', total_tax - total_many, 'денег')
