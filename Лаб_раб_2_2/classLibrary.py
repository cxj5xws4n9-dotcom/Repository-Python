# База данных книг для проверки
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"
# TODO Импортируйте и скопируйте ранее написанный класс Book


class Library:

    def __init__(self, books=None):
        """
        Конструктор библиотеки.
        Если список книг не передан, создаем пустую библиотеку.
        :param books: список книг
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        """
        Возвращает id для добавления новой книги.
        Если книг нет, возвращает 1.
        Если книги есть, возвращает id последней книги + 1.
        :return: int
        """
        if len(self.books) == 0:
            return 1
        else:
            last_book = self.books[-1]
            return last_book.id + 1

    def get_index_by_book_id(self, id_):
        """
        Возвращает индекс книги в списке по её id.
        Если книги с таким id нет, выбрасывает ValueError.
        :param id_: id книги
        :return: int
        """
        for index, book in enumerate(self.books):
            if book.id == id_:
                return index

        raise ValueError("Книги с запрашиваемым id не существует")



if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
