salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0

for month in range(1, months + 1):
    if month > 1:
        spend *= (1 + increase)
    if spend > salary:
        deficit = spend - salary
    else:
        deficit = 0
    money_capital += deficit

money_capital = round(money_capital, 2)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
