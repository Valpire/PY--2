
import doctest

class Bag:
    def __init__(self, empty_pocket: int, occupied_pocket: int):
        """создание и подготовка к работе объекта сумка
        :param empty_pocket:вместимость карманов/пустые карманы
        :param occupied_pocket: занятые карманы

        примеры:
        >>> pocket = Bag(10,0) #инициализация экземпляра класса
        """
        if not isinstance(empty_pocket, int):
            raise TypeError("количество пустых карманов должно быть типа int")
        if not empty_pocket > 0:
            raise ValueError("количество пустых карманов должно быть больше нуля")
        self.empty_pocket = empty_pocket

        if not isinstance(occupied_pocket, int):
            raise TypeError("количество вещей должно быть типа int")
        if occupied_pocket < 0:
            raise ValueError("количество пустых карманов не может быть отрицательным числом")
        self.occupied_pocket = occupied_pocket  # количество предметов в сумке

    def is_pocket_empty(self) -> bool:
        """
        функция которая проверяет является ли сумка/карманы в ней пустыми
        :return: является ли карман пустым

        примеры:
        >>> pocket = Bag(10,0)
        >>> pocket.is_pocket_empty()
        """
        ...

    def put_smth_in_the_pocket(self, things: int) -> None:
        """
        добавление вещей в карманы
        :param things: количество добавляемых вещей
        :raise ValueError: если количество добавляемых вещей превышает свободное место в карамах вызываем ошибку

        примеры:
        >>> pocket = Bag(10,0)
        >>> pocket.put_smth_in_the_pocket(5)
        """
        if not isinstance(things, int):
            raise TypeError("количество добавляемых вещей должно быть типа int")
        if things < 0:
            raise ValueError("количество добавляемых вещей должно быть положительным")
        ...

    def smth_taken_from_the_pocket(self, necessary_thing):
        """
        извлечение вещей из карманов

        :param necessary_thing: количество извлекаемых вещей
        :raise ValueError: если количество извлекаемых вещей превышает количество находящихся в караманх возвращается ошибка

        :return: количество реально извлеченных вещей

        примеры:
        >>> pocket = Bag(10,10)
        >>> pocket.smth_taken_from_the_pocket(4)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass


class Box:
    def __init__(self, capacity_volume: int, occupied_volume: int):
        """создание и подготовка к работе объекта коробка
        :param capacity_volume:вместимость коробки
        :param occupied_volume: объем занятой коробки

        примеры:
        >>> box = Bag(1000,0) #инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, int):
            raise TypeError("количество вещей в пустой коробке должно быть типа int")
        if not capacity_volume > 0:
            raise ValueError("количество свободного места должно быть больше нуля")
        self.capacity_volume = capacity_volume  # объем/вместимость коробки


        if not isinstance(occupied_volume, int):
            raise TypeError("количество вещей должно быть типа int")
        if occupied_volume < 0:
            raise ValueError("количество пустого места под вещи не может быть отрицательным числом")
        self.occupied_volume = occupied_volume  # количество предметов в коробке

    def is_box_empty(self) -> bool:
        """
        функция которая проверяет является ли коробка пустой
        :return: является ли коробка пустой

        примеры:
        >>> box = Box(1000,0)
        >>> box.is_box_empty()
        """
        ...

    def put_smth_in_the_box(self, things: int) -> None:
        """
        добавление вещей в коробку
        :param things: количество добавляемых вещей
        :raise ValueError: если количество добавляемых вещей превышает свободное место в коробке вызываем ошибку

        примеры:
        >>> box = Box(1000,0)
        >>> box.put_smth_in_the_box(300)
        """
        if not isinstance(things, int):
            raise TypeError("количество добавляемых вещей должно быть типа int")
        if things < 0:
            raise ValueError("количество добавляемых вещей должно быть положительным")
        ...

    def smth_taken_from_the_box(self, necessary_thing):
        """
        извлечение вещей из коробки

        :param necessary_thing: количество извлекаемых вещей
        :raise ValueError: если количество извлекаемых вещей превышает количество находящихся в коробке возвращается ошибка

        :return: количество реально извлеченных вещей

        примеры:
        >>> box = Box(10,10)
        >>> box.smth_taken_from_the_box(40)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass

class Basement:
    def __init__(self, empty_jar: int, filled_jar: int):
        """создание и подготовка к работе объекта подвал
        :param empty_jar:вместимость подвала
        :param filled_jar: количество банок с чем-то в подвале

        примеры:
        >>> basement = Basement(100,0) #инициализация экземпляра класса
        """
        if not isinstance(empty_jar, int):
            raise TypeError("количество банок в подвале должно быть типа int")
        if not empty_jar > 0:
            raise ValueError("количество пустого места в подвале должно быть больше нуля")
        self.empty_jar = empty_jar  # объем/вместимость подвала

        if not isinstance(filled_jar, int):
            raise TypeError("количество банок должно быть типа int")
        if filled_jar < 0:
            raise ValueError("количество пустого места под банки не может быть отрицательным числом")
        self.filled_jar = filled_jar  # количество предметов в подвале


    def is_basement_empty(self) -> bool:
        """
        функция которая проверяет является ли подвал пустым
        :return: является ли подвал пустым

        примеры:
        >>> basement = Basement(100,0)
        >>> basement.is_basement_empty()
        """
        ...

    def put_smth_in_the_basement(self, jars: int) -> None:
        """
        добавление банок в подвал
        :param jars: количество добавляемых банок
        :raise ValueError: если количество добавляемых банок превышает свободное место в подвале вызываем ошибку

        примеры:
        >>> basement = Basement(100,0)
        >>> basement.put_smth_in_the_basement(48)
        """
        if not isinstance(jars, int):
            raise TypeError("количество добавляемых банок должно быть типа int")
        if jars < 0:
            raise ValueError("количество добавляемых банок должно быть положительным")
        ...

    def smth_taken_from_the_basement(self, necessary_jars):
        """
        извлечение банок из подвала

        :param necessary_jars: количество извлекаемых банок
        :raise ValueError: если количество извлекаемых банок превышает количество находящихся в подвале возвращается ошибка

        :return: количество реально извлеченных банок

        примеры:
        >>> basement = Basement(100,100)
        >>> basement.smth_taken_from_the_basement(32)
        """
        ...

    if __name__ == "__main__":
        doctest.testmod()
        pass