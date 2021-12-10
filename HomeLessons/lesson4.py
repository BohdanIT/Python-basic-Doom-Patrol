# 1. Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    car_type = 'regular car'

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# 2. Create a child class Bus that will inherit all the variables and methods of the Vehicle class and will have seating_capacity own method

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, capacity):
        super().__init__(max_speed, mileage)
        self.capacity = capacity

    def seating_capacity(self):
        print(f'The big bus has {self.capacity} seats')


bus = Bus(150, 1200000, 75)
bus.seating_capacity()

# 3. Determine which class a given Bus object belongs to (Check type of an object)

print(type(bus))

# 4. Determine if School_bus is also an instance of the Vehicle class

school_bus = Bus(150, 110000, 50)
print(isinstance(school_bus, Vehicle))


# 5. Create a new class School with get_school_id and number_of_students instance attributes

class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


# 6*. Create a new class SchoolBus that will inherit all the methods from School and Bus and will have its own - bus_school_color

class SchoolBus(Bus, School):
    def __init__(self, max_speed, mileage, capacity, bus_color):
        super().__init__(max_speed, mileage, capacity)
        self.bus_color = bus_color

    def bus_school_color(self):
        print(f'school bus is {self.bus_school_color}')


# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method.
# Create two instances, one of Bear and one of Wolf, make a tuple of it and by using for call their action using the same method.
# Magic methods:
class Bear:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        return self.sound


class Wolf:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        return self.sound


b = Bear('bear sound')
w = Wolf('wolf sound')
bear_wolf = (b, w)

for sound in bear_wolf:
    print(sound.make_sound())


# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".

# class City:
#     def __init__(self, name, population):
#         self.name = name
#         self.population = population
#
#     def when_population(self):
#         if self.population > 1500:
#             return self.population
#         else:
#             return f"Your city is too small"
#
#
# small = City('Irpin', 1000)
# big = City("Kyiv", 5000000)
#
# cities = (small, big)
#
# for population in cities:
#     print(population.when_population())
