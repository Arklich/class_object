# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s - количество клеточек, на которое она перемещается за ход


class Turtle(object):
    pos_1 = 1
    pos_2 = 1
    col_kl = 1

    def __init__(self, x, y, s):
        self.pos_1 = x
        self.pos_2 = y
        self.col_kl = s

    def go_up(self):
        self.pos_2 += self.col_kl
        return self.pos_2

    def go_down(self):
        self.pos_2 -= self.col_kl
        return self.pos_2

    def go_left(self):
        self.col_kl -= self.col_kl
        return self.col_kl

    def go_right(self):
        self.pos_1 += self.col_kl
        return self.pos_1

    def evolve(self):
        self.col_kl += 1
        return self.col_kl

    def degrade(self):
        if self.col_kl <= 0:
            ValueError("Ошибка")
            return
        self.col_kl -= 1
        return self.col_kl

    def count_moves(self, x2, y2):
        return self.pos_1 - x2, self.pos_2 - y2

r = Turtle(5, 15, 26)

print(r.go_up())

print(r.go_down())

print(r.go_left())

print(r.go_right())

print(r.evolve())

print(r.degrade())

print(r.count_moves(12,10))



