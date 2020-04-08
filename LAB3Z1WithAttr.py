class AirLine:
    __Airplane_Type_Enum = ["None", "Airbus А320", "AirbusSSJ-100", "Boeing B787"]
    __Week_Days_Enum = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

    def __init__(self, Race_Number: int=0, DestPoint: str="None", AirPlaneType: int=0, WeekDays=[]):
        # Инициализация класса через готовые методы  Set для отслеживания исключений
        self.Race_Number = Race_Number  # не будем инкапсулировать номер рейса
        self.Dest_Point = DestPoint
        self.Airplane_Type = AirPlaneType
        self.__Week_Days = WeekDays
        print("Рейс #%s добавлен в список." % self.Race_Number)

    def __str__(self):
        s = "*" * 60
        s += "\n\tРейс #" + str(self.Race_Number) + " следующий в " + self.Dest_Point
        s += ":\n\t\tСамолетом класса: " + self.Airplane_Type
        s += "\n\t\tпо дням: " + str(self.getWeekDaysListNames() if len(self.getWeekDaysListNames()) > 0 else "не установлено.")
        s += "\n" + "*" * 60
        return s

    # контролируем ввод
    def __setattr__(self, key, value):
        if key == "Race_Number":
            self.__dict__[key] = value if value > 0 else 0
        elif key == "Dest_Point":
            self.__dict__[key] = value if value != "" else "None"
        elif key == "Airplane_Type":
            if - 1 < value < 4:
                self.__dict__[key] = self.__Airplane_Type_Enum[value]
            else:
                self.__dict__[key] = self.__Airplane_Type_Enum[0]
        elif "_AirLine__Week_Days":
            self.__dict__[key] = [False] * 7
            for i in range(len(value) if len(value) < 8 else 7):
                self.__dict__[key][i] = bool(value[i])
        else:
            print("Fuck You: ", key)

    # дни недели (set/get)
    def setWeekDays(self, WeekDays=[]):
        self.__Week_Days = WeekDays
        return self.__Week_Days

    def getWeekDays(self):
        return self.__Week_Days

    # список дней в неделе, когда совершатся вылеты
    def getWeekDaysListNames(self):
        s = []
        for i in range(len(self.__Week_Days)):
            if self.__Week_Days[i]:
                s.append(self.__Week_Days_Enum[i])
        return s

    # Есть ли вылет в определенный день
    def isOnWeekDay(self, WeekDay):
        return self.__Week_Days[WeekDay-1]



PointsDest = ["New York", "Madrid", "Minsk", "Moscow", "Los Angeles"]
WeekDaysBudni = [1,1,1,1,1]  # Будние дни
WeekDaysVih = [0,0,0,0,0,1,1]   # Выходные
WeekAllDays = WeekDaysBudni[0:5] + WeekDaysVih[5:7]  # неделя

a =[]
a.append(AirLine(452, PointsDest[2], 2, WeekDaysBudni))
a.append(AirLine(92, PointsDest[2], 3, WeekDaysVih))

a.append(AirLine(103, PointsDest[0], 1, WeekAllDays))
a.append(AirLine(4536, PointsDest[4], 1, [0,1,1,1]))
a.append(AirLine(5001, PointsDest[3], 3, [1,0,0,0,1]))

a[len(a)-1].setWeekDays([1,1,0,0,0,0,1])

print("Текущие рейсы: ", "\n".join([str(lst) for lst in a]), sep="\n")


wd = int(input("Введи день недели: "))
pn = input("Пункт назначения: ")

wdl=[]
pnl=[]
for i in a:
    if i.isOnWeekDay(wd):
        wdl.append(i.Race_Number)
    if i.Dest_Point == pn:
        pnl.append(i.Race_Number)

print("Номера рейсов летящих в " + str(wd) + " день недели:", wdl)
print("Номера рейсов летящих в " + pn + ":", pnl)
