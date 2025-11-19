import csv
import json
# TODO импортировать необходимые модули


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, encoding="utf-8") as file:
         reader = csv.DictReader(file)
         data = list(reader)# TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as file:
         json.dump(data, file, indent=4)# TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
