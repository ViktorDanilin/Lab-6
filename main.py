class guns:
    def __init__(self, bullets, f_rate, f_range):
        self.bullets = bullets
        self.f_rate = f_rate
        self.f_range = f_range

    def calculation_1(self):  # За сколько магазин опустеет
        time = self.bullets / self.f_rate * 60
        return round(time, 1)  # в секундах

    def calculation_2(self):  # Соотношение скорострельности к дальности стрельбы
        difference = self.f_rate / self.f_range
        return round(difference, 2)


class pistol(guns):  # pistol - PM (пистолет Макарова); info from wikipedia.org
    def __init__(self, bullets=8, f_rate=30, f_range=50):
        self.__bullets = bullets
        self.__f_rate = f_rate
        self.__f_range = f_range
        super().__init__(self.__bullets, self.__f_rate, self.__f_range)
        self.time = super().calculation_1()
        self.difference = super().calculation_2()

    def reload(self, bullets): # увеличиваем кол-во патронов в магазине
        self.__bullets += bullets
        super().__init__(self.__bullets, self.__f_rate, self.__f_range)
        self.time = super().calculation_1()
        print("Новое время опустошения магазина пистолета: ", self.time)
        print("_______________________________________________________")

    def print(self):
        print("Пистолет")
        print("Магазин опустеет за", self.time, "секунды")
        print("Соотношение скорострельности к дальности стрельбы: ", self.difference)
        print("_______________________________________________________")


class assault_rifle(guns):  # AR - M4; info from wikipedia.org
    def __init__(self, bullets=30, f_rate=700, f_range=500):
        self.__bullets = bullets
        self.__f_rate = f_rate
        self.__f_range = f_range
        super().__init__(self.__bullets, self.__f_rate, self.__f_range)
        self.time = super().calculation_1()
        self.difference = super().calculation_2()

    def reload(self, bullets): # увеличиваем кол-во патронов в магазине
        self.__bullets += bullets
        super().__init__(self.__bullets, self.__f_rate, self.__f_range)
        self.time = super().calculation_1()
        print("Новое время опустошения магазина штурмовой винтовки: ", self.time)
        print("_______________________________________________________")

    def print(self):
        print("Автомат")
        print("Магазин опустеет за", self.time, "секунды")
        print("Соотношение скорострельности к дальности стрельбы: ", self.difference)
        print("_______________________________________________________")


class sniper_rifle(guns):  # SR - Винтовка Мосина; info from wikipedia.org
    def __init__(self, bullets=5, f_rate=10, f_range=2000):
        self.__bullets = bullets
        self.__f_rate = f_rate
        self.__f_range = f_range
        super().__init__(self.__bullets, self.__f_rate, self.__f_range)
        self.time = super().calculation_1()
        self.difference = super().calculation_2()

    def reload(self, bullets): # увеличиваем кол-во патронов в магазине
        self.__bullets += bullets
        super().__init__(self.__bullets, self.__f_rate, self.__f_range)
        self.time = super().calculation_1()
        print("Новое время опустошения магазина снайперской винтовки: ", self.time)
        print("_______________________________________________________")

    def print(self):
        print("Снайперская винтовка")
        print("Магазин опустеет за", self.time, "секунды")
        print("Соотношение скорострельности к дальности стрельбы: ", self.difference)
        print("_______________________________________________________")


class machinepistole(guns):  # MP - MP5; info from wikipedia.org
    def __init__(self, bullets=30, f_rate=900, f_range=200):
        self.__bullets = bullets
        self.__f_rate = f_rate
        self.__f_range = f_range
        super().__init__(self.__bullets, self.__f_rate, self.__f_range)
        self.time = super().calculation_1()
        self.difference = super().calculation_2()

    def reload(self, bullets): # увеличиваем кол-во патронов в магазине
        self.__bullets += bullets
        super().__init__(self.__bullets, self.__f_rate, self.__f_range)
        self.time = super().calculation_1()
        print("Новое время опустошения магазина пп: ", self.time)
        print("_______________________________________________________")

    def print(self):
        print("Снайперская винтовка")
        print("Магазин опустеет за", self.time, "секунды")
        print("Соотношение скорострельности к дальности стрельбы: ", self.difference)
        print("_______________________________________________________")


pm = pistol()
m4 = assault_rifle()
sm = sniper_rifle()
mp5 = machinepistole()
pm.print()
pm.reload(19)
m4.print()
m4.reload(60)
sm.print()
sm.reload(10)
mp5.print()
mp5.reload(60)
