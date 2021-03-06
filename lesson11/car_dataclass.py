from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict, field
import json
import os


@dataclass(order=True)
class Car(ABC):
    current_speed = 0
    max_speed = 100
    vehicle = 'Машина'
    seats = 5

    brand: str = field(compare=False)
    model: str = field(compare=False)
    year: int = field(compare=True)
    color: str = field(compare=False)

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


@dataclass(order=True)
class Audi(Car):
    max_speed = 250
    model: str = field(compare=False)
    year: int = field(compare=True)
    color: str = field(compare=False)
    brand: str = field(compare=False)

    def brand_model(self):
        return self.brand, self.model

    def add_gas(self, add_speed: int):
        self.current_speed = min(self.current_speed + add_speed, self.max_speed + 10)
        return f'Теперь я еду со скоростью {self.current_speed} км/ч, максимальная скорость - {self.max_speed} км/ч.'

    @staticmethod
    def econ():
        return 'Включен режим ECON.'


@dataclass(order=True)
class Mercedes(Car):
    max_speed = 240
    brand: str = field(compare=False)
    model: str = field(compare=False)
    year: int = field(compare=True)
    color: str = field(compare=False)

    def brand_model(self):
        return self.brand, self.model

    def add_gas(self, add_speed: int):
        self.current_speed = min(self.current_speed + add_speed, self.max_speed + 20)
        return f'Теперь я еду со скоростью {self.current_speed} км/ч, максимальная скорость - {self.max_speed} км/ч.'

    @staticmethod
    def auto_parking():
        return 'Машина припаркуется автоматически.'


@dataclass(order=True)
class Volkswagen(Car):
    max_speed = 180
    brand: str = field(compare=False)
    model: str = field(compare=False)
    year: int = field(compare=True)
    color: str = field(compare=False)

    def brand_model(self):
        return self.brand, self.model

    def add_gas(self, add_speed: int):
        self.current_speed = min(self.current_speed + add_speed, self.max_speed - 10)
        return f'Теперь я еду со скоростью {self.current_speed} км/ч, максимальная скорость - {self.max_speed} км/ч.'

    @staticmethod
    def open_close_window():
        return 'Открытые окна автоматически закроются при закрытии машины.'


def create_car():
    audi_q5 = Audi('Audi', 'Q5', 2022, 'синий')
    mercedes_cla250 = Mercedes('Mercedes', 'CLA250', 2020, 'белый')
    volkswagen_taos = Volkswagen('Volkwagen', 'Polo', 2022, 'черный')
    car_list = [asdict(audi_q5), asdict(mercedes_cla250), asdict(volkswagen_taos)]

    def where_json(file_name):
        return os.path.exists(file_name)

    if where_json('car_list.json'):
        with open('car_list.json', 'w') as f:
            json.dump(car_list, f, indent=4, ensure_ascii=False)
    else:
        with open('car_list.json', 'w') as f:
            json.dump(car_list, f, indent=4, ensure_ascii=False)


def main():
    audi1 = Audi('Audi', 'a4', 2020, 'белый')
    audi2 = Audi('Audi', 'rs8', 2020, 'черный')
    audi2.get_max_speed = 270
    print(audi1 == audi2)

    mercedes1 = Mercedes('Mercedes', 'gl63', 2022, 'синий')
    mercedes1.get_max_speed = 250
    mercedes2 = Mercedes('Mercedes', 'cla', 2020, 'желтый')
    print(mercedes1 < mercedes2)

    volkswagen1 = Volkswagen('Volkswagen', 'taos', 2016, 'белый')
    volkswagen2 = Volkswagen('Volkswagen', 'polo', 2022, 'синий')
    volkswagen2.get_max_speed = 160
    print(volkswagen1 < volkswagen2)

    car_lst = [{
        'brand': audi1.brand,
        'model': audi1.model,
        'year': audi1.year,
        'color': audi1.color,
        'max_speed': audi1.max_speed
    },

        {
            'brand': audi2.brand,
            'model': audi2.model,
            'year': audi2.year,
            'color': audi2.color,
            'max_speed': audi2.max_speed
        },
        {
            'brand': mercedes1.brand,
            'model': mercedes1.model,
            'year': mercedes1.year,
            'color': mercedes1.color,
            'max_speed': mercedes1.max_speed
        },

        {
            'brand': mercedes2.brand,
            'model': mercedes2.model,
            'year': mercedes2.year,
            'color': mercedes2.color,
            'max_speed': mercedes2.max_speed
        },
        {
            'brand': volkswagen1.brand,
            'model': volkswagen1.model,
            'year': volkswagen1.year,
            'color': volkswagen1.color,
            'max_speed': volkswagen1.max_speed
        },
        {
            'brand': volkswagen2.brand,
            'model': volkswagen2.model,
            'year': volkswagen2.year,
            'color': volkswagen2.color,
            'max_speed': volkswagen2.max_speed
        }]

    with open('car_info.json', 'w') as f:
        json.dump(car_lst, f, indent=4, ensure_ascii=False)

    print()

    with open('car_info.json', 'r') as f:
        for item in json.load(f):
            print(f"Бренд - {item['brand']}, Модель - {item['model']}.")


create_car()

if __name__ == '__main__':
    main()
