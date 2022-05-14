from abc import ABC, abstractmethod


class Car(ABC):
    current_speed = 0
    max_speed = 100
    vehicle = 'Машина'
    seats = 5

    def __init__(self, brand, model, year, color):
        self.brand = brand.upper()
        self.model = model.upper()
        self.year = year
        self.color = color

    @classmethod
    def type_vehicle(cls):
        return f'Я - {cls.vehicle}'

    @property
    def seats_info(self):
        return f'Мое количество пассажирских мест - {self.seats}.'

    @seats_info.setter
    def seats_info(self, seats):
        self.seats = seats

    @staticmethod
    def buy_car_info(brand='', model='', year='', color=''):
        if color.endswith('ий'):
            color = color.replace('ий', 'его')
        if color.endswith('ый'):
            color = color.replace('ый', 'ого')
        long_name = f'{brand} {model} {year}'
        return f'Поздравляем с приобретением автомобиля {long_name.upper()} {color} цвета!'

    @staticmethod
    def start_car():
        return 'Машина завелась.'

    def begin_move(self):
        if self.current_speed == 0:
            return f'Моя скорость равна {self.current_speed} км/ч. Для начала движения нажмите на газ.'

    @property
    def get_max_speed(self):
        return f'Моя максимальная скорость - {self.max_speed}'

    @get_max_speed.setter
    def get_max_speed(self, max_speed):
        self.max_speed = max_speed

    def stop(self):
        self.current_speed = 0
        return 'Я остановился. Моя скорость равна 0 км/ч.'

    @staticmethod
    def emergency_signal():
        return 'Аварийная световая сигнализация включена.'

    @abstractmethod
    def add_gas(self, add_speed: int):
        pass

    @abstractmethod
    def brand_model(self):
        pass


class Audi(Car):

    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year, color)
        self.current_speed = 0
        self.max_speed = 210

    def brand_model(self):
        return self.brand, self.model

    def add_gas(self, add_speed: int):
        self.current_speed = min(self.current_speed + add_speed, self.max_speed + 10)
        return f'Теперь я еду со скоростью {self.current_speed} км/ч, максимальная скорость - {self.max_speed} км/ч.'

    @staticmethod
    def econ():
        return 'Включен режим ECON.'


class Mercedes(Car):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year, color)
        self.current_speed = 0
        self.max_speed = 200

    def brand_model(self):
        return self.brand, self.model

    def add_gas(self, add_speed: int):
        self.current_speed = min(self.current_speed + add_speed, self.max_speed + 20)
        return f'Теперь я еду со скоростью {self.current_speed} км/ч, максимальная скорость - {self.max_speed} км/ч.'

    @staticmethod
    def auto_parking():
        return 'Машина припаркуется автоматически.'


class Volkswagen(Car):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year, color)
        self.current_speed = 0
        self.max_speed = 180

    def brand_model(self):
        return self.brand, self.model

    def add_gas(self, add_speed: int):
        self.current_speed = min(self.current_speed + add_speed, self.max_speed - 10)
        return f'Теперь я еду со скоростью {self.current_speed} км/ч, максимальная скорость - {self.max_speed} км/ч.'

    @staticmethod
    def open_close_window():
        return 'Открытые окна автоматически закроются при закрытии машины.'


class Airplane(ABC):
    vehicle = 'Самолет'
    max_height = 12000

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.__engines = 2
        self.current_height = 0
        self.current_speed = 0
        self.max_speed = 850

    def amount_engines(self):
        return f'У меня {self.__engines} двигателя.'

    @classmethod
    def type_vehicle(cls):
        return f'Я - {cls.vehicle}'

    @staticmethod
    def buy_airplane_info(brand, model, color):
        if color.endswith('ий'):
            color = color.replace('ий', 'его')
        if color.endswith('ый'):
            color = color.replace('ый', 'ого')
        return f'Поздравляем с приобретением самолета {brand.upper()} {model.upper()} {color} цвета!'

    @property
    def max_height_info(self):
        return f'Моя максимальная высота полета - {self.max_height} метров.'

    @max_height_info.setter
    def max_height_info(self, max_height):
        self.max_height = max_height

    @staticmethod
    def start_airplane():
        return 'Самолет завелся.'

    def begin_move(self):
        if self.current_speed == 0:
            return f'Моя скорость равна {self.current_speed} км/ч. Для начала движения переведите рычаг скорости вверх.'

    def raise_lever(self, value_speed: int):
        self.current_speed = min(self.current_speed + value_speed, self.max_speed)
        return f'Моя скорость - {self.current_speed} км/ч, максимальная скорость - {self.max_speed} км/ч.'

    def stop(self):
        self.current_speed = 0
        return f'Я остановился. Моя скорость равна {self.current_speed} км/ч.'

    @staticmethod
    def autopilot():
        return 'Автопилот включен.'

    @abstractmethod
    def brand_model(self):
        pass

    @abstractmethod
    def close_chassis(self):
        pass


class Boeing(Airplane):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)
        self.max_speed = 900
        self.max_height = 12500

    def brand_model(self):
        return self.brand, self.model

    @staticmethod
    def passengers_capacity():
        return 'Я пассажирский самолет. Моя пассажировместимость 189 человек. '

    def close_chassis(self):
        return 'Шасси закроются автоматически.'


class Airbus(Airplane):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)
        self.max_speed = 850
        self.max_height = 11900

    def brand_model(self):
        return self.brand, self.model

    @staticmethod
    def load_capacity():
        return 'Я транспортный самолет. Моя грузоподъемность 37 тонн.'

    def close_chassis(self):
        return 'Шасси закрыты.'


class Eagle(Airplane):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)
        self.max_speed = 2650
        self.max_height = 20000

    def brand_model(self):
        return self.brand, self.model

    @staticmethod
    def feature():
        return 'Мое достоинство - скорость.'

    def close_chassis(self):
        return 'Шасси закроются автоматически на высоте 2000 метров.'


def main():
    audi1 = Audi('Audi', 'a4', '2016', 'белый')
    print(
        Audi.buy_car_info('Audi', 'a4', '2016', 'белый'),
        audi1.seats_info,
        audi1.begin_move(),
        audi1.emergency_signal(),
        sep='\n'
    )
    print()

    audi2 = Audi('Audi', 'rs8', '2020', 'черный')
    audi2.get_max_speed = 270
    audi2.seats_info = 2
    print(
        audi2.brand_model(),
        audi2.seats_info,
        audi2.get_max_speed,
        f'Моя скорость равна {audi2.current_speed} км/ч.',
        audi2.add_gas(250),
        audi2.econ(),
        audi2.stop(),
        sep='\n'
    )
    print()

    mercedes1 = Mercedes('Mercedes', 'gl63', '2020', 'синий')
    mercedes1.get_max_speed = 250
    print(
        mercedes1.buy_car_info('Mercedes', 'gl63', '2020', 'синий'),
        mercedes1.seats_info,
        f'Максимальная скорость - {mercedes1.max_speed} км/ч.',
        mercedes1.type_vehicle(), mercedes1.brand_model(),
        sep='\n'
    )
    print()

    mercedes2 = Mercedes('Mercedes', 'cla', '2020', 'желтый')
    print(
        mercedes2.start_car(),
        mercedes2.add_gas(250),
        mercedes2.auto_parking(),
        sep='\n'
    )
    print()

    volkswagen1 = Volkswagen('Volkswagen', 'taos', '2016', 'белый')
    print(
        volkswagen1.buy_car_info('Volkswagen', 'tiguan', '2016', 'белый'),
        volkswagen1.open_close_window(),
        sep='\n'
    )
    print()

    volkswagen2 = Volkswagen('Volkswagen', 'polo', '2020', 'синий')
    volkswagen2.get_max_speed = 160
    print(
        volkswagen2.start_car(),
        volkswagen2.begin_move(),
        volkswagen2.add_gas(150),
        volkswagen2.stop(),
        sep='\n'
    )
    print()

    boeing1 = Boeing('Boeing', '737', 'белый')
    boeing1.max_speed = 1100
    print(
        boeing1.buy_airplane_info('Boeing', '737', 'белый'),
        boeing1.type_vehicle(),
        boeing1.autopilot(),
        boeing1.passengers_capacity(),
        sep='\n'
    )
    print()

    boeing2 = Boeing('Boeing', '777', 'белый')
    print(
        f'Мой цвет - {boeing2.color}.',
        boeing2.close_chassis(),
        boeing2.raise_lever(1000),
        boeing2.brand_model(),
        sep='\n'
    )
    print()

    airbus1 = Airbus('Airbus', 'A300', 'серый')
    print(
        f'Моя максимальная скорость - {airbus1.max_speed} км/ч.',
        airbus1.raise_lever(250),
        airbus1.close_chassis(),
        sep='\n'
    )
    print()

    airbus2 = Airbus('Airbus', 'A380', 'черный')
    airbus2.max_speed = 780
    print(
        airbus2.load_capacity(),
        airbus2.brand_model(),
        sep='\n',
    )
    print()

    eagle1 = Eagle('Eagle', 'F-15', 'серый')
    print(
        eagle1.buy_airplane_info('Eagle', 'F-15', 'серый'),
        eagle1.max_height_info,
        eagle1.type_vehicle(),
        eagle1.feature(),
        eagle1.close_chassis(),
        sep='\n'
    )
    print()

    vehicle = [audi1,
               audi2,
               mercedes1,
               mercedes2,
               volkswagen1,
               volkswagen2,
               boeing1,
               boeing2,
               airbus1,
               airbus2,
               eagle1]

    for i in vehicle:
        print(
            i.type_vehicle(),
            i.brand_model(),
            f'[MAX_SPEED] - {i.max_speed} км/ч', '\n',
            end='_' * 58
        )
        print()


if __name__ == '__main__':
    main()
