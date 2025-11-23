def get_number(prompt: str) -> float:
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Ошибка! Необходимо ввести число. \n")

def get_operation() -> str:
    valid_operations = {"+", "-", "*", "/"}
    while True:
        operations = input("Введите операцию (+, -, *, /): ").strip()
        if operations in valid_operations:
            return operations
        print("Ошибка! Недопустимая операция. \n")

def calculate(num1: float, num2: float, operation: str) -> float:
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2

if __name__ == "__main__":
    print("Добро пожаловать в калькулятор!\n")
    num1 = get_number("Введите первое число: ")
    num2 = get_number("Введите второе число: ")
    operation = get_operation()

    if operation == "/" and num2 == 0:
        print("Ошибка! Делить на ноль нельзя!")
    else:
        result = calculate(num1, num2, operation)
        print(f"\nРезультат: {num1} {operation} {num2} = {result}")
