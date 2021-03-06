class AirLine:
    __Airplane_Type_Enum = ["None", "Airbus А320", "AirbusSSJ-100", "Boeing B787"]
    __Week_Days_Enum = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

    def __init__(self, Race_Number: int=0, DestPoint: str="None", AirPlaneType: int=0, WeekDays=[]):
        # Инициализация класса через готовые методы  Set для отслеживания исключений
        self.Race_Number = self.setRaceNumber(Race_Number)  # не будем инкапсулировать номер рейса
        self.__Dest_Point = self.setDestPoin(DestPoint)
        self.__Airplane_Type = self.setAirplaneType(AirPlaneType)
        self.__Week_Days = self.setWeekDays(WeekDays)
        print("Рейс #%s добавлен в список." % self.Race_Number)

    def __str__(self):
        s = "*" * 60
        s += "\n\tРейс #" + str(self.Race_Number) + " следующий в " + self.__Dest_Point
        s += ":\n\t\tСамолетом класса: " + self.__Airplane_Type
        s += "\n\t\tпо дням: " + str(self.getWeekDaysListNames() if len(self.getWeekDaysListNames()) > 0 else "не установлено.")
        s += "\n" + "*" * 60
        return s

    # Номер рейса (set/get)
    def setRaceNumber(self, Race_Number: int=0):
        self.Race_Number = Race_Number if Race_Number > 0 else 0
        return self.Race_Number

    def getRaceNumber(self):
        return self.Race_Number

    # пункт назначения (set/get)
    def setDestPoin(self, DestPoint: str="None"):
        self.__Dest_Point = DestPoint
        return self.__Dest_Point

    def getDestPoin(self):
        return self.__Dest_Point

    # Тип самолета (set/get)
    def setAirplaneType(self, AirPlaneType: int=0):
        if - 1 < AirPlaneType < 4:
            self.__Airplane_Type = self.__Airplane_Type_Enum[AirPlaneType]
            return self.__Airplane_Type
        return self.__Airplane_Type_Enum[0]

    def getAirplaneType(self):
        return self.__Airplane_Type

    # дни недели (set/get)
    def setWeekDays(self, WeekDays=[]):
        self.__Week_Days = [False] * 7
        for i in range(len(WeekDays) if len(WeekDays) < 8 else 7):
            self.__Week_Days[i] = bool(WeekDays[i])

        return self.__Week_Days

    def getWeekDays(self):
        return self.__Week_Days


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
WeekAllDays = WeekDaysBudni + WeekDaysVih[5:7]  # неделя


a =[]
a.append(AirLine(452, PointsDest[2], 2, WeekDaysBudni))
a.append(AirLine(92, PointsDest[2], 3, WeekDaysVih))

a.append(AirLine(103, PointsDest[0], 1, WeekAllDays))
a.append(AirLine(4536, PointsDest[4], 1, [0,1,1,1]))
a.append(AirLine(5001, PointsDest[3], 3, [1,0,0,0,1]))

print("Текущие рейсы: ", "\n".join([str(lst) for lst in a]), sep="\n")


wd = int(input("Введи день недели: "))
pn = input("Пункт назначения: ")

wdl=[]
pnl=[]
for i in a:
    if i.isOnWeekDay(wd):
        wdl.append(i.getRaceNumber())
    if i.getDestPoin() == pn:
        pnl.append(i.getRaceNumber())

print("Номера рейсов летящих в " + str(wd) + " день недели:", wdl)
print("Номера рейсов летящих в " + pn + ":", pnl)
