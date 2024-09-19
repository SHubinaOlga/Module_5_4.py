class House:  # ('ЖК Эльбрус', 30)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)
        self.value = number_of_floors


    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor > self.number_of_floors or self.new_floor < 1:
            print('"Такого этажа не существует"')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'"Название: {self.name}, кол-во этажей: {self.number_of_floors}"')

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        return self.__eq__(other) or self.__lt__(other)

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        return self

    def __radd__(self, value):
        self.number_of_floors = value + self.number_of_floors
        return self


    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    houses_history = []
    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h1.go_to(5)
# h2.go_to(10)

#h1 = House('ЖК Эльбрус', 10)
#h2 = House('ЖК Акация', 20)

# print(h1)
# print(h2)

# print(len(h1))
# print(len(h2))
#print(h1)
#print(h2)

#print(h1 == h2)  # __eq__

#h1 = h1 + 10  # __add__
#print(h1)
#print(h1 == h2)

#h1 += 10  # __iadd__
#print(h1)

#h2 = 10 + h2  # __radd__
#print(h2)

#print(h1 > h2)  # __gt__
#print(h1 >= h2)  # __ge__
#print(h1 < h2)  # __lt__
#print(h1 <= h2)  # __le__
#print(h1 != h2)  # __ne__

