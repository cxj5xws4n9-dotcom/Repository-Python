# TODO Найдите количество книг, которое можно разместить на дискете
size_disk = 1.44 #Мегабайт
pages_in_book = 100
lines_on_page = 50
symbols_in_line = 25
weight_symbol = 4 #байта

symbols_in_book = pages_in_book * lines_on_page * symbols_in_line
weight_book = round((symbols_in_book * weight_symbol) / 1024 / 1024, 2)
books_in_disk = round(size_disk / weight_book)


print("Количество книг, помещающихся на дискету:", books_in_disk)
