class Kassa:
    def __init__(self, money=0):
        self.money = money
    
    def top_up(self, x):
        self.money += x
    
    def count_1000(self):
        return self.money // 1000
    
    def take_away(self, x):
        if x > self.money:
            raise ValueError("Не достаточно денег.")
        self.money -= x

k = Kassa()
k.top_up(int(input())) # Вводим кол-во денег в кассе изначально.
print(k.count_1000()) # Вывод кол-ва целых тысяч в кассе.

k.take_away(int(input())) # Пробуем забрать меньше, чем есть в кассе для проверки остатка.
print(k.money) # Вывод текущего остатка после первого изъятия из кассы.

k.take_away(int(input())) # Пробуем забрать больше, чем есть в кассе для проверки ошибки.
