class CoffeeDrink:
    def __init__(self, coffee=0.0, water=0.0, milk_foam=0.0, steamed_milk=0.0, chocolate=0.0):
        self.__coffee = coffee
        self.__water = water
        self.milk_foam = milk_foam
        self.steamed_milk = steamed_milk
        self.chocolate = chocolate

    def make_espresso(self):
        print("Espresso made")
        self.__coffee = 0.1
        self.__water = 0.0
        self.milk_foam = 0.0
        self.steamed_milk = 0.0
        self.chocolate = 0.0

    def make_mocha(self):
        print("Mocha made")
        self.__coffee = 0.1
        self.__water = 0.0
        self.milk_foam = 0.1
        self.steamed_milk = 0.1
        self.chocolate = 0.1

    def make_macchiato(self):
        print("Macchiato made")
        self.__coffee = 0.1
        self.__water = 0.0
        self.milk_foam = 0.1
        self.steamed_milk = 0.0
        self.chocolate = 0.0

    def make_latte(self):
        print("Latte made")
        self.__coffee = 0.1
        self.__water = 0.1
        self.milk_foam = 0.1
        self.steamed_milk = 0.1
        self.chocolate = 0.0

    def make_americano(self):
        print("Americano made")
        self.__coffee = 0.1
        self.__water = 0.1
        self.milk_foam = 0.0
        self.steamed_milk = 0.0
        self.chocolate = 0.0

    def make_cappuccino(self):
        print("Cappuccino made")
        self.__coffee = 0.1
        self.__water = 0.0
        self.milk_foam = 0.1
        self.steamed_milk = 0.1
        self.chocolate = 0.0

    def add_coffee(self, amount):
        self.__coffee += amount

    def add_water(self, amount):
        self.__water += amount

    def add_milk_foam(self, amount):
        self.milk_foam += amount

    def add_steamed_milk(self, amount):
        self.steamed_milk += amount

    def add_chocolate(self, amount):
        self.chocolate += amount

    def remove_milk_foam(self):
        print("Removing milk foam")
        self.milk_foam = 0.0

    def __del__(self):
        print("Coffee drink destroyed")

    def __str__(self):
        if self.__coffee > 0 and self.__water == 0 and self.milk_foam > 0 and self.steamed_milk > 0 and self.chocolate == 0:
            return "Cappuccino"
        elif self.__coffee > 0 and self.__water == 0 and self.milk_foam == 0 and self.steamed_milk == 0 and self.chocolate == 0:
            return "Espresso"
        elif self.__coffee > 0 and self.__water > 0 and self.milk_foam > 0 and self.steamed_milk > 0 and self.chocolate == 0:
            return "Latte"
        elif self.__coffee > 0 and self.__water == 0 and self.milk_foam > 0 and self.steamed_milk > 0 and self.chocolate > 0:
            return "Mocha"
        elif self.__coffee > 0 and self.__water == 0 and self.milk_foam > 0 and self.steamed_milk == 0 and self.chocolate == 0:
            return "Macchiato"
        else:
            return "Unknown Coffee Drink"

def main():
    my_coffee = CoffeeDrink()
    
    my_coffee.make_espresso()
    print(f"Current drink: {my_coffee}")
    
    my_coffee.make_latte()
    print(f"Current drink: {my_coffee}")

    my_coffee.remove_milk_foam()
    my_coffee.make_cappuccino()
    print(f"Current drink: {my_coffee}")

    my_coffee.make_mocha()
    print(f"Current drink: {my_coffee}")

    my_coffee.add_milk_foam(0.2)
    my_coffee.add_steamed_milk(0.1)
    
    del my_coffee

main()


#2 задание
def create_grid(size):
    return [[" "] * size for _ in range(size)]

def draw_star(M):
    for i in range(7):
        M[i][3] = "*"
    M[3][:7] = ["*"] * 7

def draw_dot(M):
    M[0][2] = "."
    for i in range(1, 3):
        M[i][1:3] = ["."] * 2
    M[2][:3] = ["."] * 3

def draw_parenthesis(M):
    for i in range(1, 3):
        M[i][6:9] = [")"] * 3
    M[3][8] = ")"
    M[2][6] = " " # Clear cell

def draw_parenthesis_down(M):
    for i in range(6, 9):
        M[i][1] = "("
    for i in range(7, 9):
        M[i][2] = "("
    M[8][1:4] = ["("] * 3

def draw_rectangle(M):
    M[4][4:] = ["0"] * 6
    M[9][4:] = ["0"] * 6
    for i in range(4, 10):
        M[i][4] = "0"
        M[i][9] = "0"

def print_grid(M):
    for row in M:
        print("".join(row))

M = create_grid(10)

draw_star(M)
draw_dot(M)
draw_parenthesis(M)
draw_parenthesis_down(M)
draw_rectangle(M)
print_grid(M)

#3 задание 
def create_grid(size):
    return [[" "] * size for _ in range(size)]

def draw_eyes(M, c):
    M[3][3] = c  
    M[3][6] = c  

def draw_smile(M, c):
    M[6][3: 7] = [c]*4
    M[5][2] = c
    M[5][7] = c
  
M = create_grid(10)
draw_eyes(M, "*")
draw_smile(M, "*")

for row in M:
    print("".join(row))
#5 задание 
def F(*args):
    result = 0
    for x in args:
        result = result + x
    return result

A1, A2, A4, A8, A16, A32, A64 = 1, 2, 4, 8, 16, 32, 64
D = F(A4, A16, A64) 
print(D)
#6 задание 
def F(*args):
    result = 0
    args = sorted(args, reverse=True)
    for num in args:
        if result + num <= 51:
            result += num
        elif result - num >= 0:
            result -= num
    return result

A1, A2, A4, A8, A16, A32, A64 = 1, 2, 4, 8, 16, 32, 64
D = F(A16, A32, A2, A1)
print(D)  
#7 задание 
def F(a, b, c, n):
    x, y, z = sorted([a, b, c], reverse = True)
    result = x
    result += y if abs(n - result) > abs(n - (result + y)) else -y
    result += z if abs(n - result) > abs(n - (result + z)) else -z
    return result

#8 задание
def FA(): 
    return FD() * 8 #FD вставить
def FB():
    return 2 
def FC():
    return 3 + FE() #FE вставить
def FD():
    return 18 / FC() #FC вставить
def FE():
    return 14 / FB() #FB вставить

Y = FA() #FA вставить 
print (Y)

print(F(2, 8, 25, 19))  #вывод 19
#9 задание не уверен в нем, если что поспрашивай сделал ли кто, но вроде получилось.
def F(x, y):
    r = 0
    if F.z == 0:
        r = x + y
    if F.z == 1:
        r = x - y
    if x == y - 3:
        F.z = 1
    if x == y and y < 5:
        F.z = 0
    return r

F.z = -1
a, b, c, d = [int(x) for x in input().split()]

x = a  # Подстановка значения a в переменную x
y = b  # Подстановка значения b в переменную y

result = b - d + c - a

print(result)


#хз какое задание код номер 2

def F(*args):
    args = sorted(list(args), reverse = True)
    closeness = 0
    result = 0
    for x in args:
        if result == 0:
            result = x 
        if x != 0:
            if result == 19:
                break 
            if abs(19 - (result * x)) < closeness:
                result *= x 
            elif abs(19 - (result / x)) < closeness and result % x == 0:
                result /= x
            elif abs(19 - (result - x)) < closeness:
                result -= x 
            elif abs(19 - (result + x)) < closeness:
                result += x 
        closeness = abs(19 - result)
    return result 

X = [32, 42, 17, 19, 11, 20, 14, 16, 38, 5]
result = ""

for x in X:
    if x > 25:
        if x >= 42:
            if x > 48:
                if x <= 58:
                    result += 'Е'
                else:
                    if x == 60:
                        result += 'З' 
                    else:
                        result += 'Ж'
            else:
                result += 'И'
        else:
            if x == 40:
                result += 'Д' 
            else:
                if x <= 34:
                    if x != 28:
                        result += 'Г' 
                    else:
                        result += 'Б' 
                else:
                    result += 'А' 
    else:
        if x < 10:
            if x >= 3:
                if x != 5:
                    result += 'Н' 
                else:
                    result += 'М'
            else:
                if x > 0:
                    result += 'К' 
                else:
                    result += 'Л' 
        else:
            if x >= 17:
                if x > 20:
                    result += 'Р' 
                else:
                    result += 'П' 
            else:
                if x <= 14:
                    result += 'О'
                else:
                    result += 'Т'
print(result)

class RR:
    def __init__(self, salty, fresh):
        self.salty = salty
        self.fresh = fresh
    
    def show(self):
        print(f'Соленый: {self.salty}, Пресный: {self.fresh}')


class Fish(RR):
    def __init__(self, salty, fresh, name, edible, inedible, predatory, nonpredatory):
        super().__init__(salty, fresh)
        self.name = name
        self.edible = edible
        self.inedible = inedible
        self.predatory = predatory
        self.nonpredatory = nonpredatory
    
    def show(self):
        super().show()
        print(f'Название: {self.name}, Съедобная: {self.edible}, Несъедобная: {self.inedible}, Хищная: {self.predatory}, Не хищная: {self.nonpredatory}')


class Jellyfish(RR):
    def __init__(self, salty, fresh, species, poisonous, nonpoisonous):
        super().__init__(salty, fresh)
        self.species = species
        self.poisonous = poisonous
        self.nonpoisonous = nonpoisonous

    def show(self):
        super().show()
        print(f'Вид: {self.species}, Ядовитая: {self.poisonous}, Неядовитая: {self.nonpoisonous}')


class Mollusc(RR):
    def __init__(self, salty, fresh, name, edible, nonedible, racovina, nonracovina):
        super().__init__(salty, fresh)
        self.name = name
        self.edible = edible
        self.nonedible = nonedible
        self.racovina = racovina
        self.nonracovina = nonracovina

    def show(self):
        super().show()
        print(f'Название: {self.name}, Съедобная: {self.edible}, Несъедобная: {self.nonedible}, Раковина: {self.racovina}, Нет раковины: {self.nonracovina}')


fish = Fish('селедка', 'съедобная', 'Имя рыбы', 'да', 'нет', 'да', 'нет')
jellyfish = Jellyfish('розовая', 'ядовитая', 'Вид медузы', 'да', 'нет')
mollusc = Mollusc('красный', 'съедобный', 'Имя моллюска', 'да', 'нет', 'да', 'нет')

fish.show()
jellyfish.show()
mollusc.show()


import math

class AB:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class L(AB):
    def __init__(self, x, y, x1, y1):
        super().__init__(x, y)
        self.x1 = x1
        self.y1 = y1

    def length(self):
        return math.sqrt((self.x1 - self.x) ** 2 + (self.y1 - self.y) ** 2)

class S(L):
    def __init__(self, x, y, x1, y1):
        super().__init__(x, y, x1, y1)

    def square(self):
        a = self.length()
        return math.pi * a ** 2

class V(L):
    def __init__(self, x, y, x1, y1):
        super().__init__(x, y, x1, y1)

    def volume(self):
        a = self.length()
        return (1/3) * math.pi * a ** 2

line = L(1, 3, 2, 0)
square = S(2, 3, 4, 5)
volume = V(4, 3, 2, 1)

print(line.length())
print(square.square())
print(volume.volume())
