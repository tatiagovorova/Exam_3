def Palindrome(a):
    if a[::-1] == a[::]:
        return 'Палиндром'
    else:
        return "Не палиндром"
b = str(input('Введите слово: '))
print(Palindrome(b))

def creditcard(a):
    print(("*" * (len(a[:-4]))) + a[-4:])
a = int(input("Номер карты: "))
a = str(a)
creditcard(a)

#Класс Tomato
#1.Класс Tomato
class Tomato:
#2.states:Стадии созревания
    states = {1: "зелёный", 2: "на стадии созревания", 3: "созрел"}
#3. Метод __init__()
    def __init__(self, index):
        self._index = index
        self._state = 1

    def growing(self):
        if self._state < 3:
            self._state += 1
        self.result_of_growing()

    def result_of_growing(self):
        print(f"Помидор {self._index} {Tomato.states[self._state]}")
#4. Метод grow():Переход на следующую стадию созревания
    def grow(self):
        self.growing()
#5. Метод is_ripe(): Проверка на полное созревание томата
    def is_ripe(self):
        if self._state == 3:
            return True
        else:
            return False
#Класс TomatoBush
#1.Класс TomatoBush
class TomatoBush:
#2.Метод init: список объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num-1)]
#3.Метод grow_all: Перевод всех томатов на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
#4.Метод all_are_ripe(): Проверка - все ли томаты стали спелыми
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])
#5.Метод give_away_all: Сбор урожая
    def give_away_all(self):
        self.tomatoes = []

#Класс Gardener
#1.Класс Gardener
class Gardener:
#2.Метод init
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
#3.Метод work: Выращивание растения
    def work(self):
        print("Садовник полил томат")
        self._plant.grow_all()
        print("Садовник вырастил томат")
#4.Метод harvest: Сбор урожая

