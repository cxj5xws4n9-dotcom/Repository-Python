import doctest


class Stack:
    def __init__(self, max_size: int):
        """
        Создание объекта "Стек"

        :param max_size: Максимальный размер стека

        Примеры:
        >>> stack = Stack(3)
        """
        if not isinstance(max_size, int):
            raise TypeError("Размер стека должен быть int")
        if max_size <= 0:
            raise ValueError("Размер стека должен быть положительным")
        self.max_size = max_size
        self.items = []

    def push(self, item: object) -> None:
        """
        Добавляет элемент в стек.

        :param item: Любой объект
        :return: None

        Примеры:
        >>> stack = Stack(2)
        >>> stack.push(10)
        >>> stack.push(20)
        >>> stack.items
        [10, 20]
        """
        if len(self.items) >= self.max_size:
            raise ValueError("Стек переполнен")
        self.items.append(item)

    def pop(self) -> object:
        """
        Удаляет и возвращает верхний элемент стека.

        :return: Удаленный элемент

        Примеры:
        >>> stack = Stack(2)
        >>> stack.push(5)
        >>> stack.pop()
        5
        """
        if len(self.items) == 0:
            raise ValueError("Стек пуст")
        return self.items.pop()

    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек.

        :return: True если пуст, иначе False

        Примеры:
        >>> stack = Stack(1)
        >>> stack.is_empty()
        True
        """
        return len(self.items) == 0


if __name__ == "__main__":
    doctest.testmod()
