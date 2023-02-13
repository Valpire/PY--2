from typing import Union


class Plane:
    def __init__(self, fuel_amount: Union[int, float], fuel_consumption: Union[int, float]):
        """
        Создание и подготовка к работе объекта "самолет"
        :param fuel_amount_amount: текущее количество топлива в баке
        :param fuel_consumption: потребление топлива на единицу пути
        """
        self._fuel_amount = None  # protected, т к меняется только при заправке/совершении полета
        self._init_fuel_amount(fuel_amount)

        self._fuel_consumption = None  # protected, т к это неизменная характеристика самолета
        self._init_fuel_consumption(fuel_consumption)

    def __str__(self) -> str:
        """
        Печатный вид экземпляра класса
        """
        return f"самолет. Количество топлива {self.fuel_amount} л. Потребление топлива {self.fuel_consumption} л/км"

    def __repr__(self) -> str:
        """
        Вид экземпляра класса при применении repr()
        """
        return f"{self.__class__.__name__}(fuel_amount={self.fuel_amount}, fuel_consumption={self.fuel_consumption})"

    def _init_fuel_amount(self, fuel_amount: Union[int, float]) -> None:
        """
        Инициализация protected атрибута _fuel_amount - текущее количество топлива
        Protected из-за того, что используется только при инициализации экземпляра класса
        :param fuel_amount: текущее количество топлива
        """
        if not isinstance(fuel_amount, (int, float)):
            raise TypeError('Количество топлива должно быть типа int или float')
        if fuel_amount < 0:
            raise ValueError('Количество топлива должно быть не меньше 0')
        self._fuel_amount = fuel_amount

    def _init_fuel_consumption(self, fuel_consumption: Union[int, float]) -> None:
        """
        Инициализация protected атрибута _fuel_consumption - потребление топлива на единицу пути
        Protected метод из-за того, что используется только при инициализации экземпляра класса
        :param fuel_consumption: потребление топлива на единицу пути
        """
        if not isinstance(fuel_consumption, (int, float)):
            raise TypeError('Потребление топлива должно быть типа int или float')
        if fuel_consumption <= 0:
            raise ValueError('Потребление топлива должно быть больше 0')
        self._fuel_consumption = fuel_consumption

    @property
    def fuel_amount(self) -> Union[int, float]:
        """
        getter для protected атрибута _fuel_amount
        setter не используется, т к protected атрибут
        """
        return self._fuel_amount

    @property
    def fuel_consumption(self) -> Union[int, float]:
        """
        getter для protected атрибута _fuel_consumption
        setter не используется, т к protected атрибут
        """
        return self._fuel_consumption

    def add_fuel(self, extra_fuel: Union[int, float]) -> None:
        """
        Добавить топлива в бак
        Публичный метод
        :param extra_fuel: дополнительное топливо
        """
        if not isinstance(extra_fuel, (int, float)):
            raise TypeError('Добавленное топливо должно быть типа int или float')
        if extra_fuel < 0:
            raise ValueError('Добавленное топливо должно быть не меньше 0')
        self._fuel_amount += extra_fuel

    def taking_flight(self, distance: Union[int, float]) -> None:
        """
        Совершить полет длиной distance, соответственно потратив некоторое количество топлива
        Публичный метод
        :param distance: длина пути
        """
        if not isinstance(distance, (int, float)):
            raise TypeError('Длина пути должна быть типа int или float')
        if distance < 0:
            raise ValueError('Длина пути должна быть не меньше 0')
        ...


class PassengerPlane(Plane):
    def __init__(self, fuel_amount: Union[int, float], fuel_consumption: Union[int, float], seats: int):
        """
        Создание и подготовка к работе объекта класса "Пассажирский самолет", унаследован от класса "самолет"
        :param fuel_amount: текущее количество топлива в баке
        :param fuel_consumption: потребление топлива на единицу пути
        :param seats: количество мест в самолете
        """
        super().__init__(fuel_amount, fuel_consumption)
        self._seats = None  # protected, т к это неизменная характеристика самолета
        self._init_seats(seats)

    def __repr__(self) -> str:
        """
        Вид экземпляра класса при применении repr()
        Перегрузка метода базового класса
        """
        return f"{self.__class__.__name__}(fuel_amount={self.fuel_amount}, " \
               f"fuel_consumption={self.fuel_consumption}, seats={self.seats})"

    def _init_seats(self, seats: int) -> None:
        """
        Инициализация protected атрибута _seats - количество мест в самолете
        Protected метод из-за того, что используется только при инициализации экземпляра класса
        :param seats: количество мест в самолете
        """
        if not isinstance(seats, int):
            raise TypeError('Количество мест в самолете должно быть типа int')
        if seats <= 0:
            raise ValueError('Количество мест в самолете должно быть больше 0')
        self._seats = seats

    @property
    def seats(self) -> int:
        """
        getter для protected атрибута _seats
        setter не используется, т к protected атрибут
        """
        return self._seats

    def taking_flight(self, distance: Union[int, float]) -> None:
        """
        Совершить полет длиной distance, соответственно потратив некоторое количество топлива
        Перегрузка метода базового класса, т к совершаем полет на пассажирском самолете
        Публичный метод
        :param distance: длина пути
        """
        if not isinstance(distance, (int, float)):
            raise TypeError('Длина пути должна быть типа int или float')
        if distance < 0:
            raise ValueError('Длина пути должна быть не меньше 0')
        ...


class CargoPlane(Plane):
    def __init__(self, fuel_amount: Union[int, float], fuel_consumption: Union[int, float], capacity: Union[int, float]):
        """
        Создание и подготовка к работе объекта класса "Грузовой самолет", унаследован от класса "самолет"
        :param fuel_amount: текущее количество топлива в баке
        :param fuel_consumption: потребление топлива на единицу пути
        :param capacity: грузоподъемность
        """
        super().__init__(fuel_amount, fuel_consumption)
        self._capacity = None  # protected, т к это неизменная характеристика самолета
        self._init_capacity(capacity)

    def __repr__(self) -> str:
        """
        Вид экземпляра класса при применении repr()
        Перегрузка метода базового класса
        """
        return f"{self.__class__.__name__}(fuel_amount={self.fuel_amount}, " \
               f"fuel_consumption={self.fuel_consumption}, capacity={self.capacity})"

    def _init_capacity(self, capacity: Union[int, float]) -> None:
        """
        Инициализация protected атрибута _capacity - грузоподъемность
        Protected метод из-за того, что используется только при инициализации экземпляра класса
        :param capacity: грузоподъемность
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError('Грузоподъемность самолета должна быть типа int или float')
        if capacity <= 0:
            raise ValueError('Грузоподъемность самолета должна быть больше 0')
        self._capacity = capacity

    @property
    def capacity(self) -> Union[int, float]:
        """
        getter для protected атрибута _capacity
        setter не используется, т к protected атрибут
        """
        return self._capacity

    def taking_flight(self, distance: Union[int, float]) -> None:
        """
        Совершить полет длиной distance, соответственно потратив некоторое количество топлива
        Перегрузка метода базового класса, т к совершаем полет на грузовом самолете
        Публичный метод
        :param distance: длина пути
        """
        if not isinstance(distance, (int, float)):
            raise TypeError('Длина пути должна быть типа int или float')
        if distance < 0:
            raise ValueError('Длина пути должна быть не меньше 0')
        ...

if __name__ == "__main__":
    # Write your solution here
    pass
