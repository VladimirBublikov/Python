class Lejbnic:
    def __init__(self, numcount = 2):
        self.n = 0
        self.sumvalue = 0
        self.currentvalue = 0
        self.numcount = numcount

    def __iter__(self):
        import math

        while math.trunc(math.fabs(math.pi/4 - self.sumvalue) * 10**self.numcount) > 0:
            self.currentvalue = (-1)**(self.n)/(self.n*2 + 1)
            self.sumvalue += self.currentvalue
            self.n += 1

            # вернем кортеж: сумма  / значение / номер
            yield round(self.sumvalue,  self.numcount+2), round(self.currentvalue, self.numcount+2), self.n


# вызываем генератор (точность приближения 2 знака к ожидаемой сумме пи на 4)
for number in Lejbnic(2):
    val, c, n = number
    print(n, ":  сумма = ", val, "; значение элемента: ", c)
