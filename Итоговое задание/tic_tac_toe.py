import random


class Board:
    """
    Класс игрового поля 3x3 для игры "Крестики-нолики".
    """

    def __init__(self):
        """
        Создаёт пустое игровое поле.
        """
        self.grid = [[None, None, None],
                     [None, None, None],
                     [None, None, None]]

    def display_board(self) -> None:
        """
        Выводит игровое поле в консоль.
        """
        print("\nТекущее поле:")
        for row in self.grid:
            row_str = []
            for cell in row:
                if cell is None:
                    row_str.append(".")
                else:
                    row_str.append(cell)
            print(" ".join(row_str))
        print()

    def is_valid_move(self, x: int, y: int) -> bool:
        """
        Проверяет, можно ли сделать ход в клетку (x, y).

        :param x: строка
        :param y: столбец
        :return: True, если ход возможен, иначе False
        """
        if x < 0 or x > 2 or y < 0 or y > 2:
            return False
        if self.grid[x][y] is not None:
            return False
        return True

    def make_move(self, x: int, y: int, symbol: str) -> None:
        """
        Ставит символ на поле.

        :param x: строка
        :param y: столбец
        :param symbol: символ игрока ("X" или "O")
        """
        self.grid[x][y] = symbol

    def check_full(self) -> bool:
        """
        Проверяет, заполнено ли поле полностью.

        :return: True, если поле заполнено, иначе False
        """
        for row in self.grid:
            for cell in row:
                if cell is None:
                    return False
        return True

    def check_winner(self, symbol: str) -> bool:
        """
        Проверяет, есть ли победа у указанного символа.

        :param symbol: "X" или "O"
        :return: True, если есть выигрышная комбинация
        """
        # Проверка строк
        for row in self.grid:
            if row[0] == row[1] == row[2] == symbol:
                return True

        # Проверка столбцов
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] == symbol:
                return True

        # Проверка диагоналей
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == symbol:
            return True
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == symbol:
            return True

        return False

    def reset(self) -> None:
        """
        Очищает игровое поле.
        """
        self.grid = [[None, None, None],
                     [None, None, None],
                     [None, None, None]]


class Player:
    """
    Базовый класс игрока.
    """

    def __init__(self, name: str, symbol: str):
        """
        :param name: Имя игрока
        :param symbol: Символ игрока ("X" или "O")
        """
        self.name = name
        self.symbol = symbol

    def get_name(self) -> str:
        """
        :return: Имя игрока
        """
        return self.name

    def get_symbol(self) -> str:
        """
        :return: Символ игрока
        """
        return self.symbol

    def make_move(self, board: Board) -> None:
        """
        Сделать ход (будет переопределён в дочерних классах).
        """
        raise NotImplementedError("Метод должен быть реализован в дочернем классе")


class HumanPlayer(Player):
    """
    Игрок-человек.
    """

    def make_move(self, board: Board) -> None:
        """
        Запрашивает ввод координат у пользователя и делает ход.
        Обрабатывает ошибки ввода.
        """
        while True:
            try:
                print(f"{self.name}, ваш ход. Введите координаты (строка и столбец от 0 до 2).")
                x = int(input("Строка: "))
                y = int(input("Столбец: "))

                if board.is_valid_move(x, y):
                    board.make_move(x, y, self.symbol)
                    break
                else:
                    print("Нельзя сделать ход в эту клетку. Попробуйте снова.")
            except ValueError:
                print("Ошибка ввода. Нужно ввести числа от 0 до 2.")


class AIPlayer(Player):
    """
    Игрок-компьютер.
    Делает случайный допустимый ход.
    """

    def make_move(self, board: Board) -> None:
        """
        Выбирает случайную свободную клетку и делает ход.
        """
        print(f"{self.name} (компьютер) делает ход...")

        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)

            if board.is_valid_move(x, y):
                board.make_move(x, y, self.symbol)
                break


class Game:
    """
    Основной класс игры "Крестики-нолики".
    """

    def __init__(self):
        self.board = Board()
        self.player1 = None
        self.player2 = None
        self.current_player = None

    def start_game(self) -> None:
        """
        Запускает игру: создаёт игроков и начинает игровой цикл.
        """
        print("Добро пожаловать в игру 'Крестики-нолики'!")

        name1 = input("Введите имя первого игрока: ")
        print("Выберите режим игры:")
        print("1 - Игрок против игрока")
        print("2 - Игрок против компьютера")

        mode = input("Ваш выбор: ")

        if mode == "2":
            self.player1 = HumanPlayer(name1, "X")
            self.player2 = AIPlayer("Компьютер", "O")
        else:
            name2 = input("Введите имя второго игрока: ")
            self.player1 = HumanPlayer(name1, "X")
            self.player2 = HumanPlayer(name2, "O")

        self.current_player = self.player1
        self.board.reset()

        self.game_loop()

    def game_loop(self) -> None:
        """
        Основной игровой цикл.
        """
        while True:
            self.board.display_board()
            self.play_turn()

            if self.check_winner():
                self.board.display_board()
                self.display_result()
                break

            self.switch_player()

    def play_turn(self) -> None:
        """
        Выполняет один ход текущего игрока.
        """
        self.current_player.make_move(self.board)

    def switch_player(self) -> None:
        """
        Переключает текущего игрока.
        """
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def check_winner(self) -> bool:
        """
        Проверяет, есть ли победитель или ничья.

        :return: True, если игра закончена, иначе False
        """
        if self.board.check_winner(self.current_player.get_symbol()):
            return True

        if self.board.check_full():
            return True

        return False

    def display_result(self) -> None:
        """
        Выводит результат игры.
        """
        if self.board.check_winner(self.current_player.get_symbol()):
            print(f"Победил игрок {self.current_player.get_name()}!")
        else:
            print("Ничья!")

    def reset_game(self) -> None:
        """
        Перезапускает игру.
        """
        self.board.reset()
        self.current_player = self.player1


if __name__ == "__main__":
    game = Game()
    game.start_game()
