import random

# Constructor to initialize the Person object with name, age, money, and home ownership status
class Person:
    def __init__(self, name, age, money, has_home):
        self.name = name
        self.age = age
        self.money = money
        self.has_home = has_home

    # Method to print the person's information
    def provide_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Money: {self.money}")
        print(f"Has home: {self.has_home}")

    # Method to increase the person's money
    def make_money(self, amount):
        self.money += amount

    def buy_home(self, cost):
        if self.money >= cost:
            self.money -= cost
            self.has_home = True
            print("Congratulations! You have bought a new home.")
        else:
            print("Sorry, you don't have enough money to buy this home.")


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def apply_discount(self, discount):
        self.cost -= discount


class Realtor:
    instance = None
    houses = []

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = Realtor()
            cls.houses = [House(40, 50000), House(50, 75000), House(60, 100000)]
        return cls.instance

    def provide_info(self):
        print("Available houses:")
        for i, house in enumerate(self.houses):
            print(f"House {i + 1}: Area {house.area}m2, Cost {house.cost}")

    def give_discount(self, house_index, discount):
        house = self.houses[house_index - 1]
        house.apply_discount(discount)
        print(f"Discount of {discount} applied to House {house_index}. New cost: {house.cost}")

    def steal_money(self):
        if random.random() < 0.1:
            print("Oops! The realtor has stolen your money!")
            return True
        else:
            return False


# Example usage
person = Person("Anna", 17, 120000, False)
realtor = Realtor.get_instance()

person.provide_info()
realtor.provide_info()
realtor.give_discount(1, 10000)
realtor.give_discount(2, 20000)
person.buy_home(realtor.houses[0].cost)
person.provide_info()

if realtor.steal_money():
    person.money = 0

person.provide_info()  
