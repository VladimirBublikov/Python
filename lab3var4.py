class cvetok():
    def __init__(self, dlina: float, cvetokname):
        # cvetokname - тип цветка (роза, хризантема)
        # dlina - стебель, его длина

        self.stebel = dlina
        self.cvetokname = cvetokname

    def __str__(self):
        return self.cvetokname



# объекты цветков
c1 = cvetok(20, "Роза")
c2 = cvetok(14, "Хризантема")

# список цветков, он же букет
buket = []
buket.append(cvetok(20, "Роза"))
buket.append(cvetok(23, "Алая роза"))
buket.append(cvetok(19, "Белая роза"))
buket.append(c1)
buket.append(c2)

print(",". join(str(i) for i in buket))
