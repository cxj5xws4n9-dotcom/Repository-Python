import doctest


class Timer:
    def __init__(self, seconds: int):
        """
        Создание объекта "Таймер"

        :param seconds: Количество секунд

        Примеры:
        >>> t = Timer(10)
        """
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть int")
        if seconds < 0:
            raise ValueError("Секунды не могут быть отрицательными")
        self.seconds = seconds

    def tick(self, value: int) -> None:
        """
        Уменьшает таймер на указанное количество секунд.

        :param value: Сколько секунд прошло
        :return: None

        Примеры:
        >>> t = Timer(10)
        >>> t.tick(3)
        >>> t.seconds
        7
        """
        if not isinstance(value, int):
            raise TypeError("Значение должно быть int")
        if value < 0:
            raise ValueError("Значение не может быть отрицательным")

        self.seconds -= value
        if self.seconds < 0:
            self.seconds = 0

    def is_finished(self) -> bool:
        """
        Проверяет, закончился ли таймер.

        :return: True если таймер равен 0, иначе False

        Примеры:
        >>> t = Timer(0)
        >>> t.is_finished()
        True
        """
        return self.seconds == 0


if __name__ == "__main__":
    doctest.testmod()
